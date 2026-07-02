import telebot
from dotenv import load_dotenv
import os
load_dotenv()
TOKEN=os.environ['TOKEN']
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['photo'])
def send_bot(message):
    if not message.photo:
        return bot.send_message(message.chat.id,'нужно отправить фотоЛОЛ')
    file_info = bot.get_file(message.photo[-1].file_id)
    file_name = file_info.file_path.split('/')[-1] 
    downloaded_file = bot.download_file(file_info.file_path) 
    with open(file_name, 'wb') as new_file:
        new_file.write(downloaded_file)
    with open(file_name, 'rb') as new_file:
        bot.send_photo(message.chat.id,new_file)
bot.polling()
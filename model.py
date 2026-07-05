from imageai.Detection import ObjectDetection
import cv2

detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath("yolov3.pt")
detector.loadModel()
def detect_animals(image_in,image_out):
  detections = detector.detectObjectsFromImage(image_in,None,minimum_percentage_probability=33)
  def analyze_objects(detections):
    want = [
    'bird',
    'cat',
    'dog',
    'horse',
    'sheep',
    'cow',
    'elephant',
    'bear',
    'zebra',
    'giraffe',]
    return [detection for detection in detections if detection['name'] in want]
  detections = analyze_objects(detections)
  img = cv2.imread(image_in)
  for detection in detections:
    x1,y1,x2,y2 = detection['box_points']
    cv2.rectangle(img,(x1,y1),(x2,y2),color = (0,255,0),thickness=2)
    cv2.putText(img,detection['name'],(x1,y1 - 5),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (91,102,104), 2)
  cv2.imwrite(image_out,img)
  return image_out
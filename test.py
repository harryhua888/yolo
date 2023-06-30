from ultralytics import YOLO
import cv2

# Load a model
model = YOLO('yolov8n.onnx')
#model = YOLO('runs\detect\\train25\weights\\best.onnx')
model = YOLO('scp/weights/best.onnx')
model = YOLO('scp-3/best.onnx')

results = model('poisonTestImages\\006843.png')
boxes = results[0].boxes

print(boxes)



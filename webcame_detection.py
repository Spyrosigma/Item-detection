from ultralytics import YOLO
from predict import DetectionPredictor
import cv2

model = YOLO("yolov8n.pt")

results = model.predict(source='0',show=True) #accepts all format : img, folder, videos
print(results)


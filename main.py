from ultralytics import YOLO

model = YOLO('yolov8s.pt')

# Training
results = model.train(
   data='C:/Users/Shahbaz Satti/Downloads/dataset2/data.yaml',
   imgsz=640,
   epochs=50,
   batch=8,
   name='yolov8s-50e'
)


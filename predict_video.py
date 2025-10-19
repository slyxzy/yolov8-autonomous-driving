from ultralytics import YOLO

# Load the trained model
model = YOLO('C:/Users/Shahbaz Satti/runs/detect/yolov8s-50e8/weights/best.pt')

# Perform inference on the video
results = model.predict(
    source='C:/Users/Shahbaz Satti/Downloads/cityDriving.mp4',  # Path to the video file
    show=True,                            # Display the output in real-time
    imgsz=1280,                           # Set the image size for inference
    save=True,                            # Save the output
    hide_labels=True,                     # Hide labels in the output
    name='yolov8s_50e_infer1280'       # Name for the run
)

# Save the results
results.save()
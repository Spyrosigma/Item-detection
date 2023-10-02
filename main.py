from flask import Flask, render_template, request
from PIL import Image
from ultralytics import YOLO
import os
from predict import DetectionPredictor
import cv2

# Load a pretrained YOLOv8n model
model = YOLO('yolov8n.pt')

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

#-------------------THIS IS FOR IMAAAAAAGEEEEEEEEEE DETECTION !!----------------
@app.route("/image_detection")
def image():
    i = 'image.jpg'
    results = model(i)  # results list
    # Show the results
    for r in results:
        im_array = r.plot()  # plot a BGR numpy array of predictions
        im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
        im.show()  # show image

#-------------------THIS IS FOR VIDEOOOOOOOOO DETECTION !!----------------
@app.route("/video_detection")
def video():
    # Open the video file
    video_path = 'video.mp4'
    cap = cv2.VideoCapture(video_path)

    # Loop through the video frames
    while cap.isOpened():
        # Read a frame from the video
        success, frame = cap.read()

        if success:
            # Run YOLOv8 inference on the frame
            results = model(frame)

            # Visualize the results on the frame
            annotated_frame = results[0].plot()

            # Display the annotated frame
            cv2.imshow("YOLOv8 Inference", annotated_frame)

            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        else:
            # Break the loop if the end of the video is reached
            break

    # Release the video capture object and close the display window
    cap.release()
    cv2.destroyAllWindows()

#-------------------This is for webcame !!--------------------
@app.route("/webcame")
def webcame():
    results = model.predict(source='0',show=True) #accepts all format : img, folder, videos
    print(results)

app.run(debug=True)
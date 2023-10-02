from flask import Flask, render_template, request, jsonify
from PIL import Image
from ultralytics import YOLO
import os
# Load a pretrained YOLOv8n model
model = YOLO('yolov8n.pt')
def image_detection(image):
    #THIS IS FOR IMAAAAAAGEEEEEEEEEE DETECTION !!
    results = model(image)  # results list
    # Show the results
    for r in results:
        im_array = r.plot()  # plot a BGR numpy array of predictions
        im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
        im.show()  # show image

#----------------FLASK APP HERE----------------
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        # Check if an image file is uploaded
        if 'image' not in request.files:
            return jsonify({'error': 'No image part'})

        image = request.files['image']

        # If the user does not select a file, the browser submits an empty part without a filename
        if image.filename == '':
            return jsonify({'error': 'No selected file'})

        # Process the uploaded image using your YOLO detection code
        detection_result = image_detection(image)

        # You can return the detection results as JSON or render an HTML template with the results
        return jsonify({'result': detection_result})

    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)

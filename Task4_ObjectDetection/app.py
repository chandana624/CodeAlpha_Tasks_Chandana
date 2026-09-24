from flask import Flask, render_template, request
from ultralytics import YOLO
import os
import cv2

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
RESULT_FOLDER = "static/results"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

model = YOLO("yolo11n.pt")


@app.route("/", methods=["GET", "POST"])
def home():
    result_image = None

    if request.method == "POST":
        file = request.files.get("image")

        if file and file.filename:
            input_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(input_path)

            results = model.predict(source=input_path)

            annotated_image = results[0].plot()

            output_filename = "detected_" + file.filename
            output_path = os.path.join(RESULT_FOLDER, output_filename)

            cv2.imwrite(output_path, annotated_image)

            result_image = f"/static/results/{output_filename}"

    return render_template("index.html", result_image=result_image)


if __name__ == "__main__":
    app.run(debug=True)

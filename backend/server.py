from flask import Flask, request, jsonify, send_file
import cv2
import numpy as np
import os
from io import BytesIO
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

app = Flask(__name__)


def detect_lines(image):
    img_g = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img_canny = cv2.Canny(img_g, 300, 450)
    lines = cv2.HoughLines(img_canny, rho=1, theta=np.pi / 360, threshold=100)
    fig, ax = plt.subplots()
    ax.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    if lines is not None:
        for i in lines:
            rho = i[0][0]
            theta = i[0][1]
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = rho * a
            y0 = rho * b
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))
            ax.plot([x1, x2], [y1, y2], color="red")
    canvas = FigureCanvas(fig)
    output = BytesIO()
    canvas.print_png(output)
    plt.close(fig)
    return output.getvalue()


@app.route("/upload", methods=["POST"])
def upload_image():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400
    image = Image.open(file.stream)
    image = np.array(image)
    processed_image = detect_lines(image)
    return send_file(BytesIO(processed_image), mimetype="image/png")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

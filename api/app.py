from flask import Flask, request, render_template
from app_helper_model import *
from werkzeug.utils import secure_filename
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler("logs/logs.log"), logging.StreamHandler()],
)

logger = logging.getLogger(__name__)


app = Flask(__name__)


@app.route("/")
def index():
    '''jgghjg'''
    return render_template("index.html")


@app.route("/uploader", methods=["POST"])
def upload_file():
    '''Das '''
    predictions = ""
    if request.method == "POST":
        f = request.files["file"]
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, "static", "uploads", secure_filename(f.filename)
        )
        f.save(file_path)
        predictions = get_predictions(file_path)
    return render_template(
        "upload.html", predictions=predictions, display_image=f.filename
    )


if __name__ == "__main__":
    app.run()

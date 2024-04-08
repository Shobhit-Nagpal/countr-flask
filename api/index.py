from flask import Flask, request
from markupsafe import escape
from utils.model import load_model

app = Flask(__name__)
model = load_model()


@app.get("/")
def index():
    return f"Model is {model}"

@app.post("/count/image")
def countImage():
    return "Count image"

@app.post("/count/video")
def countVideo():
    return "Count video"

if __name__ == '__main__':
    app.run()

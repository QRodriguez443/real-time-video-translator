from pytube import YouTube, exceptions
from flask import Flask, request
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)
app.debug = True

def extract_stream(url):
    while True:
        youtube = YouTube(url)
        try:
            video = youtube.streams.first()
        except exceptions.VideoUnavailable as e:
            print("I am thrown")
            time.sleep(1)

            
    streaming_url = video.url

@app.route("/url", methods=["POST"])
def get_url():
    url = request.form.get("url")
    # Retrieve URL of video if user is currently on the relevant page
    extract_stream(url)
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
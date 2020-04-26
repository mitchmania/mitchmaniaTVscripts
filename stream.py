from flask import Flask
import os
import subprocess
import threading


vid_dir = "../mnt"

app = Flask(__name__)

current_video = ""

@app.route("/")
def main_route():
    return current_video

def callFFmpeg(filename: str):
    global current_video
    current_video = filename
    ffmpeg_process = subprocess.Popen([
        "/usr/bin/ffmpeg",
        "-re",
        "-i",
        filename,
        "-c",
        "copy",
        "-f",
        "flv",
        "rtmp://192.168.1.178:1935/app/test"
        ])
    ffmpeg_process.wait()


def main():
    threading.Thread(target=app.run).start()
    while(1):
        for root, _, files in os.walk(os.path.abspath("../mnt")):
            for filename in files:
                if filename.endswith(".mp4"):
                    abs_path = os.path.join(root, filename)
                    callFFmpeg(abs_path)

if __name__ == "__main__":
    main()

    
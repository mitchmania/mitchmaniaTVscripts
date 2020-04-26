import os
import subprocess


vid_dir = "../mnt"

current_video = ""

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


def stream_main():
    while(1):
        for root, _, files in os.walk(os.path.abspath("../mnt")):
            for filename in files:
                if filename.endswith(".mp4"):
                    abs_path = os.path.join(root, filename)
                    callFFmpeg(abs_path)    
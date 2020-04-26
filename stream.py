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


def stream_main(my_pl):
    while(1):
        callFFmpeg(my_pl.get_next_vid())
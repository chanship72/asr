import argparse
import os
import tempfile
import time

from moviepy.editor import VideoFileClip
# from openai import OpenAI

from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

target_video = "bc_pmlyj_7-1.mp4"

def split_video(video_path, temp_dir, duration=120):
    print("\033[92mStarting to split into mp3 files every 5 minutes!\033[0m")
    video = VideoFileClip(video_path)
    for i in range(0, int(video.duration), duration):
        chunk_filename = os.path.join(temp_dir, f"chunk_{i//duration}.mp3")
        clip = video.subclip(i, min(i + duration, int(video.duration)))
        clip.audio.write_audiofile(chunk_filename)

split_video(target_video, "./data")
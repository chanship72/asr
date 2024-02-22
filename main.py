import io
import os
import numpy as np

try:
    import tensorflow  # required in Colab to avoid protobuf compatibility issues
except ImportError:
    pass

import torch
import pandas as pd
import urllib
import tarfile
import whisper
import torchaudio

from scipy.io import wavfile
from tqdm.notebook import tqdm

import whisper
import pytube
import jiwer
import csv
import nlptutti as metrics

audio_file = "data/chunk_0.mp3"

model = whisper.load_model("large-v3")
# model = whisper.load_model("base")
# model = whisper.load_model("tiny")

result = model.transcribe(audio_file, language="ko", verbose=0, fp16 = False)
hypothesis = result["text"]

print("hypothesis_whisper:",hypothesis)

d = {}
with open('bc_pmlyj_7-1.txt', 'r', encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    for row in csv_reader:
        d[row[0]] = row[1:]

reference = ""
for key,value in d.items():
    # print(key, value)
    if len(value) > 0:
        reference += value[0]
    if key == '00:01:54': break

print("reference:",reference)

result = metrics.get_wer(reference, hypothesis)
wer = result['wer']

print(f"Word Error Rate (WER) :", wer)
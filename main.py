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
import jiwer
import csv
import nlptutti as metrics
import ssl
from transformers import BartConfig
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import pipeline

# checkpoint = 'theSOL1/kogrammar-base'
# tokenizer = AutoTokenizer.from_pretrained(checkpoint)
# config = BartConfig.from_pretrained(checkpoint)
# model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint, config=config, device_map='auto')
# pipe = pipeline('text2text-generation', model=model, tokenizer=tokenizer)

ssl._create_default_https_context = ssl._create_unverified_context
# audio_file = "data/500209_2024_03_1.mp4"
audio_file = "data/500209_2024_03_1.mp4"
model = whisper.load_model("large-v3")
# model = whisper.load_model("base")
# model = whisper.load_model("tiny")

result = model.transcribe(audio_file, language="ko", verbose=0, fp16 = False)
hypothesis = result["text"]
print("hypothesis_whisper:",hypothesis)

# total_length, split_length  = len(hypothesis), 15
# split_hypothesis = [hypothesis[i:i+split_length] for i in range(0, total_length , split_length)]
# final_result = ""
# for i,words in enumerate(split_hypothesis):
#     corrected_text = pipe(words)[0]

#     final_result = final_result + corrected_text['generated_text'][:-1] + " "
# print(final_result)

# d = {}
# with open('bc_pmlyj_7-1.txt', 'r', encoding="utf-8") as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter='\t')
#     for row in csv_reader:
#         d[row[0]] = row[1:]

# reference = ""
# for key,value in d.items():
#     # print(key, value)
#     if len(value) > 0:
#         reference += value[0]
#     if key == '00:01:54': break

# print("reference:",reference)

# result = metrics.get_wer(reference, hypothesis)
# wer = result['wer']

# print(f"Word Error Rate (WER) :", wer)
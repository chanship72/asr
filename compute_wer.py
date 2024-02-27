import os
import jiwer
import nlptutti as metrics
import csv

whisper_path = "./result"
final_path = "./final"
naver_path = "./naver"

whisper_file_list = os.listdir(whisper_path)
print ("whisper_file_list: {}".format(whisper_file_list))

# def getDataFromFile(mpath, fname):
#     d = {}
#     with open(mpath+"/"+fname, 'r', encoding="utf-8") as csv_file:
#         csv_reader = csv.reader(csv_file, delimiter='\t')
#         prev_row = 0
#         for row in csv_reader:
#             if row[0].startswith('00' or '01'):
#                 d[row[0]] = row[1:]
#                 prev_row = row[0]
#             else:
#                 d[prev_row] = row[0]
            
#     text_str = ""
#     for key,value in d.items():
#         if len(value) > 0:
#             text_str += str(value[0])
#     return text_str

def getData(mpath, fname):
    print(fname)
    f = open(mpath+"/"+fname, 'r', encoding='utf-8')
    data = f.read()
    f.close()
    return data    

for fname in whisper_file_list:
    print(fname)
    hypothesis_whisper = getData(whisper_path, fname)
    hypothesis_naver = getData(naver_path, fname[:-4]+"_out.txt")
    reference = getData(final_path, fname[:-4]+"_out.txt")

    print("hypothesis_whisper:",hypothesis_whisper[:50])
    print("hypothesis_naver:",hypothesis_naver[:50])
    print("reference:",reference[:50])

    result = metrics.get_wer(hypothesis_naver, reference)
    wer = result['wer']

    print(f"[naver]Word Error Rate (WER) :", wer)

    result = metrics.get_wer(hypothesis_whisper, reference)
    wer = result['wer']

    print(f"[whisper]Word Error Rate (WER) :", wer)
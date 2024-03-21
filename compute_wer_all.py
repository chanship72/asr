import os
import jiwer
import nlptutti as metrics
import csv

# whisper_path = "./result"
# final_path = "./final"
# naver_path = "./naver"

# whisper_file_list = os.listdir(whisper_path)
# print ("whisper_file_list: {}".format(whisper_file_list))

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
    f = open(mpath+fname, 'r')
    data = f.read()
    f.close()
    return data    

parent_path = './PoCTesting/'

for i in [1,2,3]:
    # try:
    hypothesis_whisper = getData(parent_path, "airaw"+str(i)+".txt")
    hypothesis_naver = getData(parent_path, "naver_worst"+str(i)+".txt")
    reference = getData(parent_path, "answer"+str(i)+".txt")

    # print("hypothesis_whisper:",hypothesis_whisper[:50])
    # print("hypothesis_naver:",hypothesis_naver[:50])
    # print("reference:",reference[:50])

    result = metrics.get_wer(hypothesis_naver, reference)
    wer = result['wer']
    substitutions = result['substitutions']
    deletions = result['deletions']
    insertions = result['insertions']
    print("[naver]Word Error Rate (WER) : {} | substitutions: {} | deletions: {} | insertions: {}".format(wer, substitutions, deletions, insertions))

    result = metrics.get_wer(hypothesis_whisper, reference)
    wer = result['wer']
    substitutions = result['substitutions']
    deletions = result['deletions']
    insertions = result['insertions']

    print("[whisper]Word Error Rate (WER) : {} | substitutions: {} | deletions: {} | insertions: {}".format(wer, substitutions, deletions, insertions))
    # except:
    #     print("file read error")
    #     print("")
    #     continue
        
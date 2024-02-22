import csv

d = {}
with open('bc_pmlyj_7-1.txt', 'r', encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    for row in csv_reader:
        d[row[0]] = row[1:]
        
text_str = ""
for key,value in d.items():
    # print(key, value)
    if len(value) > 0:
        text_str += value[0]
    if key == '00:01:54': break
print(text_str)
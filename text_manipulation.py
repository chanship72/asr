import csv


def getDataFromFile(fname):
    d = {}
    with open(fname, 'r', encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        for row in csv_reader:
            if row[0].startswith('00' or '01'):
                d[row[0]] = row[1:]
            else:
                d[prev_row] += str(row[1:])
            prev_row = row[0]
            
    text_str = ""
    for key,value in d.items():
        # print(key, value)
        if len(value) > 0:
            text_str += str(value[0])
    return text_str    
print(getDataFromFile('bc_pmlyj_7-1.txt'))

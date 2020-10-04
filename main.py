import csv

"""
with open('c:/Users/chirag saxena/Desktop/Probabilty lab/RELIANCE.csv', 'r') as f:
    read = csv.reader(f)
    interestingrows=[row for idx, row in enumerate(read) if idx in (22,41)]
    for row in read:
        if(row[0]=='04-08-2020'):
            print(float(row[4]))
    for i in range(22,41):
        print(row[4])
print(interestingrows[4])
print(type(row))"""
cleanD=[]
with open('c:/Users/chirag saxena/Desktop/Probabilty lab/RELIANCE.csv') as fd:
    reader=csv.reader(fd)
    interestingrows=[row for idx, row in enumerate(reader) if idx in (41,40,39,38,37,36,35,34,33,32,31,30,29,28,27,26,25,24,23,22,21,20)]

    for i in range(0,21):
       cleanD.append(interestingrows[i][4])
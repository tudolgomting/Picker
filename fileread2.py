import os

try:
    listFile = open("model.list2", 'r')
    line = listFile.readline()
    
    if len(line) > 0:
        
        lists = line.split()
        
        for x in lists:
            print(x)

import os

try:
    listFile = open("model.list", 'r')
    for modelName in listFile.readlines():
        if len(modelName) > 0:
            print(modelName)
        else:
            break
except Error as e:
    print(e)

'''
    writer = csv.writer(csvFile)
    writer.writerow(('number', 'plus2', 'times2'))
    for i in range(10):
        writer.writerow((i, i+2, i*2))
finally:
    listFile.close()
'''

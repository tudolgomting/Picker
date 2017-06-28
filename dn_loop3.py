import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Sample resource
# source file url ~ http://www.japanesebeauties.net/japanese/kasumi-arimura/10/kasumi-arimura-11.jpg
# target file location ~ [down/kasumi-arimura/kasumi-arimura-1.jpg] 1 ~ 12

headUrl = "http://www.japanesebeauties.net/japanese/"
#imageCounter = 12
imageCounter = 2

pageCounter = 2

#modelName = "kasumi-arimura"
modelName = "yua-aida"

fileLocation = "down" + "/" + modelName
#fileLocation = "down"


#directory = os.path.dirname(fileLocation)
directory = fileLocation
print("[directory    ] " + directory)

if not os.path.exists(directory):
    os.makedirs(directory)

fileSize = 1000000
newImgCounter = 0
for cnt1 in range(1, pageCounter+1):
    for cnt2 in range(1, imageCounter+1):
        
        imageLocation = headUrl + modelName + "/%d/" % cnt1
        imageLocation = imageLocation + modelName + "-%d" % cnt2 + ".jpg"
        print("[imageLocation] " + imageLocation)
        
        newImgCounter = newImgCounter + 1
        downloadPath = fileLocation + "/" + modelName + "-%06d.jpg" % newImgCounter
        print("[downloadPath ] " + downloadPath)
        
        try:
            urlretrieve(imageLocation, downloadPath)
            print("----------------------------------------------------------")
            
            fileSize = os.path.getsize(downloadPath)
            if fileSize < 100000:
                #if image size lower than 100KB, it's not a image what looking for. stop looping.
                print("% % Image size is lower than 100KB. STOP downloading. % %")
                break
        except Exception as e:
            print(e)
            continue  # continue to next
            fileSize = os.path.getsize(downloadPath)

    if fileSize < 100000:
        #if image size lower than 100KB, it's not a image what looking for. stop looping.
        print("% % Image size is lower than 100KB. Break Outer Loop. % %")
        break

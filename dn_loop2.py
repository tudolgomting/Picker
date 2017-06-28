import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Sample resource
# <img src="http://www.japanesebeauties.net/japanese/kasumi-arimura/10/kasumi-arimura-11.jpg"><br>
# <img src="http://www.japanesebeauties.net/japanese/kasumi-arimura/10/kasumi-arimura-12.jpg"><br>
# target file location ~ [down/kasumi-arimura/kasumi-arimura-1.jpg] 1 ~ 12

headUrl = "http://www.japanesebeauties.net/japanese/"
imageCounter = 12

pageCounter = 301
modelName = "kasumi-arimura"

#fileLocation = "down" + "/" + modelName
fileLocation = "down"


#directory = os.path.dirname(fileLocation)
directory = fileLocation
print("[directory    ] " + directory)

if not os.path.exists(directory):
    os.makedirs(directory)

    
newImgCounter = 0
for cnt1 in range(300, pageCounter+1):
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
        except Exception, e:
            print e
            continue  # continue to next

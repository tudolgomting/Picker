import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

downloadDirectory = "down"
#baseUrl = "http://pythonscraping.com"
baseUrl = "http://www.japanesebeauties.net/model/kasumi-arimura/6"
#baseUrl = "http://www.japanesebeauties.net/search.php?model=kasumi+arimura&type=Photos"

def getAbsoluteURL(baseUrl, source):
    
    print("getAbsoluteURL().[source] " + source)
    
    if source.startswith("http://www."):
        #url = "http://" + source[11:]
        url = source
        print("getAbsoluteURL().[1_url ] " + url)
    elif source.startswith("http://"):
        url = source
        #print("(2) url: "+url)
        print("getAbsoluteURL().[2_url ] " + url)
#    elif source.startswith("https://www."):
#        url = "https://" + source[11:]
#        print("(3) url: "+url)
#    elif source.startswith("https://"):
#        url = source
#        print("(4) url: "+url)
    elif source.startswith("www."):
        #url = source[4:]
        url = "http://" + source
        print("getAbsoluteURL().[5_url ] " + url)
    else:
        url = baseUrl + "/" + source
        print("getAbsoluteURL().[9_url ] " + url)
    
    if baseUrl not in url:
        url = baseUrl
        return url
    return url

def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
    try:
        print("getDownloadPath().[baseUrl    ] " + str(baseUrl))
        print("getDownloadPath().[absoluteUrl] " + str(absoluteUrl))
        print("getDownloadPath().[directory  ] " + str(downloadDirectory))
        
        if absoluteUrl is not None:
            path = absoluteUrl.replace("www.", "")
        else:
            path = ""
        print("getDownloadPath().[path 1     ] " + str(path))
        
        path = path.replace(baseUrl, "")
        print("getDownloadPath().[path 2     ] " + str(path))
        
        path = downloadDirectory + path
        print("getDownloadPath().[path 3     ] " + str(path))
        
        #baseUrlLen = len(baseUrl)
        baseUrlLen = len("http://www.japanesebeauties.net")
        path = downloadDirectory + path[baseUrlLen:]
        print("getDownloadPath().[path 4     ] " + str(path))
        
        
        directory = os.path.dirname(path)

        if not os.path.exists(directory):
            os.makedirs(directory)
            
    except AttributeError as e:
        path = ""
        return path
    except TypeError as e:
        path = ""
        return path
    
    return path


#html = urlopen("http://www.pythonscraping.com")
#html = urlopen("http://www.japanesebeauties.net")
html = urlopen("http://www.japanesebeauties.net/model/kasumi-arimura/6/")
#html = urlopen("http://www.japanesebeauties.net/search.php?model=kasumi+arimura&type=Photos")

bsObj = BeautifulSoup(html, "html5lib")
downloadList = bsObj.findAll(src=True)

counter = 1
for download in downloadList:
    if counter <= 3:
        counter = counter + 1
    else:
        break
        
    fileUrl = getAbsoluteURL(baseUrl, download["src"])
    #print("fileUrl ~~ ["+fileUrl+"]")
    print("baseUrl ~~ ["+baseUrl+"]")
    print("Directory  ["+downloadDirectory+"]")
    print("--------------------------------------------")
    if fileUrl is not None:
        print("fileUrl ~~ ["+fileUrl+"]")
        print("baseUrl ~~ ["+baseUrl+"]")
        print("Directory  ["+downloadDirectory+"]")
    try:
        downPath = getDownloadPath(baseUrl, fileUrl, downloadDirectory)
        print("downPath   ["+downPath+"]")
        print(" ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
        urlretrieve(fileUrl, downPath)
    except TypeError as e:
        print("TypeError: "+str(e))

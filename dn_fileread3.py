import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

def downloadImages(mName):
	headUrl = "http://www.japanesebeauties.net/japanese/"
	
	imageCounter = 12
	
	pageStart = 1
	pageCounter = 20
	
	modelName = mName
	
	fileLocation = "Documents/down/" + modelName
	#fileLocation = "down"
	
	#directory = os.path.dirname(fileLocation)
	directory = fileLocation
	print("[directory    ] " + directory)
	
	if not os.path.exists(directory):
		os.makedirs(directory)
	
	fileSize = 1000000
	newImgCounter = 0
	for cnt1 in range(pageStart, pageCounter+1):
		for cnt2 in range(1, imageCounter+1):
		
			imageLocation = headUrl + modelName + "/%d/" % cnt1
			imageLocation = imageLocation + modelName + "-%d" % cnt2 + ".jpg"
			print("[imageLocation] " + imageLocation)
			
			newImgCounter = newImgCounter + 1
			downloadPath = fileLocation + "/" + modelName + "-%04d.jpg" % newImgCounter
			print("[downloadPath ] " + downloadPath)
			
			try:
				urlretrieve(imageLocation, downloadPath)
				print("----------------------------------------------------------")
			
				fileSize = os.path.getsize(downloadPath)
				if fileSize < 50000:
					#if image size lower than 100KB, it's not a image what looking for. stop looping.
					print("% % Image size is lower than 100KB. STOP downloading. % %")
					break
			except Exception as e:
				print(e)
				continue  # continue to next
				
		#fileSize = os.path.getsize(downloadPath)
		if fileSize < 50000:
			#if image size lower than 100KB, it's not a image what looking for. stop looping.
			print("% % Image size is lower than 100KB. Break Outer Loop. % %")
			break

try:
	listFile = open("model.list", 'r')
	line = listFile.readline()
	
	if len(line) > 0:
		lists = line.split(",")
	else:
		print("file[model.list] is empty..!!")
		exit(0)
	
	for x in lists:
		if len(x) > 0:
			print(x)
			print("-------")
			downloadImages(x)
		else:
			print("No more model names..")
			break

except Error as e:
	print(e)

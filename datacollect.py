from pynput.keyboard import Key, Listener
from datetime import datetime
import json
from dataprocess import dataProcess, extractTimings
import time
import os

keyPressData = []
keyReleaseData = []

def createFile(directory, data, entry):
	filename = '{0}/data{1}.json'.format(directory, entry + 1)
	with open(filename, 'a') as f:
		json.dump(data, f)


def createDirectory(index):
	for user in range(1,12):
		directory = 'user{0}/text{1}'.format(user, index + 1)
		if not os.path.exists(directory):
			os.makedirs(directory)
			return directory
		else:
			continue

def onPress(key):
	t = datetime.now()
	if not key == Key.enter:
		time = t.minute*60*(10**6) + t.second*(10**6) + t.microsecond
		keyPressData.append("p-{0}-{1}".format(key,time))

def onRelease(key):
	t = datetime.now()
	if key == Key.enter:
		return False
	else:
		time = t.minute*60*(10**6) + t.second*(10**6) + t.microsecond
		keyReleaseData.append("r-{0}-{1}".format(key,time))

def dataCollect():
	global keyPressData
	global keyReleaseData

	textList = [r"abu@9,l12$", "the person and great for government know skill new have year even about from for make which people how not", "student hello world", r"world%99, 12@hello; why.not72, #dream5$0* people@16love* 32great#%have"]

	for index, text in enumerate(textList):
		directory = createDirectory(index)
		print("Entry 40 times:")
		
		for entry in range(40):
			print('{0}------'.format(text))
			with Listener(on_press=onPress, on_release=onRelease) as listener:
				listener.join()
			
			data = dict(keyPressData=keyPressData, keyReleaseData=keyReleaseData)
			createFile(directory, data, entry)
			keyPressData = []
			keyReleaseData = []
			time.sleep(5)

if __name__ == '__main__':
	dataCollect()
from pynput.keyboard import Key, Listener
from datetime import datetime
import json
from dataprocess import dataProcess, extractTimings
import time
import os

keyPressData = []
keyReleaseData = []
dataset = []

def processAndStore(keyPressData, keyReleaseData):
	keyPressData, keyReleaseData = extractTimings(dataProcess(keyPressData), dataProcess(keyReleaseData))
	data = dict(keyPressData=keyPressData, keyReleaseData=keyReleaseData)
	dataset.append(data)

def onPress(key):
	t = datetime.now()
	# print("p-{0}".format(key))
	if not key == Key.enter:
		time = t.minute*60*(10**6) + t.second*(10**6) + t.microsecond
		keyPressData.append("p-{0}-{1}".format(key,time))
	# if key == Key.enter:
	#     return False

def onRelease(key):
	t = datetime.now()
	# print("r-{0}".format(key))
	if key == Key.enter:
		return False
	else:
		time = t.minute*60*(10**6) + t.second*(10**6) + t.microsecond
		keyReleaseData.append("r-{0}-{1}".format(key,time))

def dataCollect():
	global keyPressData
	global keyReleaseData
	global dataset

	for user in range(1,11):
		directory = 'user{0}'.format(user)
		if not os.path.exists(directory):
			os.makedirs(directory)
			break
		else:
			continue

	# text = input("Enter training text: ")
	textList = [r"abu@9,l12$", "the person and great for government know skill new have year even about from for make which people how not", "'your name' hello world", r"world%99, 12@hello; why.not72, #dream5$0* people@16love* 32great#%have"]
	for index, text in enumerate(textList):
		print("Enter 40 times:")
		for entry in range(40):
			print('{0}------'.format(text))
			
			with Listener(on_press=onPress, on_release=onRelease) as listener:
				listener.join()
			
			processAndStore(keyPressData, keyReleaseData)
			keyPressData = []
			keyReleaseData = []
			time.sleep(4)

		# create json file; since this a static model and text is always same
		# therefore it is not added to the json object

		filename = '{0}/data{1}.json'.format(directory, index + 1)
		with open(filename, 'a') as f:
			json.dump(dataset, f)

		for index, dataentry in enumerate(dataset):
			print("{0}----{1}".format(index + 1, dataentry))

		dataset = []

dataCollect()
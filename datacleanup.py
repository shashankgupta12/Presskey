import json
from dataprocess import dataProcessKeyPress, dataProcessKeyRelease, removeExtraShift, swapShift, removeExtraKeys
from difflib import SequenceMatcher as sm
import os

def createDirectoryStructure():
	directory = 'processedData'
	if not os.path.exists(directory):
		os.makedirs(directory)
		for user in range(1,12):
			direc = '{0}/user{1}'.format(directory, user)
			os.makedirs(direc)

def processText1(directory, newDirectory):
	count = 0
	for i in range(1,41):
		filename = '{0}data{1}.json'.format(directory, i)
		if not os.path.isfile(filename):
			continue
		data = json.load(open(filename, 'r'))
		keyPressData, keyReleaseData = data['keyPressData'], data['keyReleaseData']
		if len(keyPressData) > 6 and len(keyReleaseData) > 6:
			keyPressData, keyReleaseData = removeExtraKeys(dataProcessKeyPress(keyPressData)), removeExtraKeys(dataProcessKeyRelease(keyReleaseData))
			keyPressData, keyReleaseData = swapShift(*removeExtraShift(keyPressData, keyReleaseData))
			kp = ''.join([i.split('-')[1] for i in keyPressData]).replace('\'','')
			kr = ''.join([i.split('-')[1] for i in keyReleaseData]).replace('\'','')
			pressString = ['abuKey.shift@9,l12Key.shift$', 'abuKey.shift_r@9,l12Key.shift_r$']
			if sm(None, pressString[0], kp).ratio() > 0.95 or sm(None, pressString[1], kp).ratio() > 0.95:
				count += 1
	print(count)

def processText2(directory, newDirectory):
	count = 0
	for i in range(1,41):
		filename = '{0}data{1}.json'.format(directory, i)
		if not os.path.isfile(filename):
			continue
		data = json.load(open(filename, 'r'))
		keyPressData, keyReleaseData = data['keyPressData'], data['keyReleaseData']
		if len(keyPressData) > 15 and len(keyReleaseData) > 15:
			keyPressData, keyReleaseData = removeExtraKeys(dataProcessKeyPress(keyPressData)), removeExtraKeys(dataProcessKeyRelease(keyReleaseData))
			kp = ''.join([i.split('-')[1] for i in keyPressData]).replace('\'','')
			kr = ''.join([i.split('-')[1] for i in keyReleaseData]).replace('\'','')
			pressString = ['theKey.spacepersonKey.spaceandKey.spacegreatKey.spaceforKey.spacegovernmentKey.spaceknowKey.spaceskillKey.spacenewKey.spacehaveKey.spaceyearKey.spaceevenKey.spaceaboutKey.spacefromKey.spaceforKey.spacemakeKey.spacewhichKey.spacepeopleKey.spacehowKey.spacenot']
			if sm(None, pressString[0], kp).ratio() > 0.95:
				count += 1
	print(count)

def processText3(directory, newDirectory):
	count = 0
	for i in range(1,41):
		filename = '{0}data{1}.json'.format(directory, i)
		if not os.path.isfile(filename):
			continue
		data = json.load(open(filename, 'r'))
		keyPressData, keyReleaseData = data['keyPressData'], data['keyReleaseData']
		if len(keyPressData) > 6 and len(keyReleaseData) > 6:
			keyPressData, keyReleaseData = removeExtraKeys(dataProcessKeyPress(keyPressData)), removeExtraKeys(dataProcessKeyRelease(keyReleaseData))
			kp = ''.join([i.split('-')[1] for i in keyPressData]).replace('\'','')
			kr = ''.join([i.split('-')[1] for i in keyReleaseData]).replace('\'','')
			pressString = ['studentKey.spacehelloKey.spaceworld']
			if sm(None, pressString[0], kp).ratio() > 0.95:
				count += 1
	print(count)

def processText4(directory, newDirectory):
	count = 0
	for i in range(1,41):
		filename = '{0}data{1}.json'.format(directory, i)
		if not os.path.isfile(filename):
			continue
		data = json.load(open(filename, 'r'))
		keyPressData, keyReleaseData = data['keyPressData'], data['keyReleaseData']
		if len(keyPressData) > 15 and len(keyReleaseData) > 15:
			keyPressData, keyReleaseData = removeExtraKeys(dataProcessKeyPress(keyPressData)), removeExtraKeys(dataProcessKeyRelease(keyReleaseData))
			keyPressData, keyReleaseData = swapShift(*removeExtraShift(keyPressData, keyReleaseData))
			kp = ''.join([i.split('-')[1] for i in keyPressData]).replace('\'','')
			kr = ''.join([i.split('-')[1] for i in keyReleaseData]).replace('\'','')
			pressString = [r'worldKey.shift%99,Key.space12Key.shift@hello;Key.spacewhy.not72,Key.spaceKey.shift#dream5Key.shift$0Key.shift*Key.spacepeopleKey.shift@16loveKey.shift*Key.space32greatKey.shift#Key.shift%have', r'worldKey.shift_r%99,Key.space12Key.shift_r@hello;Key.spacewhy.not72,Key.spaceKey.shift_r#dream5Key.shift_r$0Key.shift_r*Key.spacepeopleKey.shift_r@16loveKey.shift_r*Key.space32greatKey.shift_r#Key.shift_r%have']
			if sm(None, pressString[0], kp).ratio() > 0.90 or sm(None, pressString[1], kp).ratio() > 0.90:
				count += 1
	print(count)

def dataCleanup():
	createDirectoryStructure()
	for eachuser in range(1,12):
		directory = ['userData/user{0}/text1/'.format(eachuser), 'userData/user{0}/text2/'.format(eachuser), 'userData/user{0}/text3/'.format(eachuser), 'userData/user{0}/text4/'.format(eachuser)]
		newDirectory = ['processedData/user{0}/text1/'.format(eachuser), 'processed/user{0}/text2/'.format(eachuser), 'processed/user{0}/text3/'.format(eachuser), 'processed/user{0}/text4/'.format(eachuser)]
		processText1(directory[0], newDirectory[0])
		processText2(directory[1], newDirectory[1])
		processText3(directory[2], newDirectory[2])
		processText4(directory[3], newDirectory[3])
		print()

if __name__ == '__main__':
	dataCleanup()
import json 
import os
from calculatetimings import calculateInterkeyTime
import matplotlib.pyplot as plt

def createDirectoryStructure():
	directory = 'boxplots'
	if not os.path.exists(directory):
		os.makedirs(directory)
		for text in range(1,5):
			direc = '{0}/text{1}'.format(directory, text)
			os.makedirs(direc)

def removeOutliers():
	for text in range(1, 5):
		for user in range(1, 12):
			filename = 'processedData/text{0}/user{1}.json'.format(text, user)
			with open(filename, 'r') as f:
				data = [json.loads(line) for line in f]
			all_ikt = [calculateInterkeyTime(timings['keyPressData'], timings['keyReleaseData']) for timings in data]
			ikt = [list(lst) for lst in zip(*all_ikt)]
			for data in ikt:
				print(len(data))
				plt.figure()
				plt.boxplot(data)
				plt.savefig('boxplots/text{0}/user{1}.png'.format(text, user))
			print()

if __name__ == '__main__':
	createDirectoryStructure()
	removeOutliers()
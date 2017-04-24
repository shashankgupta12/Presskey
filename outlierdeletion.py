import json 
import os
from calculatetimings import calculateInterkeyTime
import matplotlib.pyplot as plt
import numpy

def createDirectoryStructure():
	directory = 'boxplots'
	if not os.path.exists(directory):
		os.makedirs(directory)
		for text in range(1, 5):
			direc = '{0}/text{1}'.format(directory, text)
			os.makedirs(direc)
			for user in range(1, 12):
				dire = '{0}/user{1}'.format(direc, user)
				os.makedirs(dire)

def checkOutliers():
	for text in range(1, 5):
		for user in range(1, 12):
			filename = 'processedData/text{0}/user{1}.json'.format(text, user)
			with open(filename, 'r') as f:
				data = [json.loads(line) for line in f]
			all_ikt = [calculateInterkeyTime(timings['keyPressData'], timings['keyReleaseData']) for timings in data]
			ikt = [list(lst) for lst in zip(*all_ikt)]
			for index, data in enumerate(ikt):
				plt.figure()
				plt.boxplot(data)
				plt.savefig('boxplots/text{0}/user{1}/{2}.png'.format(text, user, index))

def getPositionOfOutliers(text, user):
	filename = 'processedData/text{0}/user{1}.json'.format(text, user)
	with open(filename, 'r') as f:
		data = [json.loads(line) for line in f]
	all_ikt = [calculateInterkeyTime(timings['keyPressData'], timings['keyReleaseData']) for timings in data]
	ikt = [list(lst) for lst in zip(*all_ikt)]
	outliers = []
	for data in ikt:
		a = numpy.array(data)
		q1 = numpy.percentile(a, 25)
		q3 = numpy.percentile(a, 75)
		iqr = q3 - q1
		outliers.extend([index for index, item in enumerate(data) if item > q3 + (1.5*iqr) or item < q1 - (1.5*iqr)])
	return list(set(outliers))

if __name__ == '__main__':
	createDirectoryStructure()
	checkOutliers()
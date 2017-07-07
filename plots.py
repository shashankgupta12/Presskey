from calculatetimings import calculateInterkeyTime, calculateKeyHoldTime
import json
import matplotlib.pyplot as plt
from outlierdeletion import getPositionOfOutliers

def plotOfBoxplots():
	filename = 'processedData/text{0}/user{1}.json'.format(3, 1)
	with open(filename, 'r') as f:
		data = [json.loads(line) for line in f]
	
	all_ikt = [[i/10000 for i in calculateInterkeyTime(timings['keyPressData'], timings['keyReleaseData'])] for timings in data]
	ikt = [list(lst) for lst in zip(*all_ikt)]
	
	plt.figure()
	plt.boxplot(ikt, vert=0)
	my_yticks = ['s-t', 't-u', 'u-d', 'd-e', 'e-n', 'n-t', 't-space', 'space-h', 'h-e', 'e-l', 'l-l', 'l-o', 'o-space', 'space-w', 'w-o', 'o-r', 'r-l', 'l-d']
	plt.yticks(list(range(1, 19)), my_yticks)
	plt.xlabel('Range of interkey values')
	plt.ylabel('Box plots')
	plt.show()

def profilePlot():
	all_keyHoldTime = []
	all_interkeyTime = []
	
	for user in range(1, 12):
		for text in range(1, 5):
			filename = 'processedData/text{0}/user{1}.json'.format(text, user)
			with open(filename, 'r') as f:
				data = [json.loads(line) for line in f]
			
			outliers = getPositionOfOutliers(text, user)
			data = [timings for i, timings in enumerate(data) if not i in outliers]

			for i, timings in enumerate(data):
				ikt = calculateInterkeyTime(timings['keyPressData'], timings['keyReleaseData'])
				kht = calculateKeyHoldTime(timings['keyPressData'], timings['keyReleaseData'])
				
				if len(ikt) > len(kht):
					del ikt[-1]
				elif len(kht) > len(ikt):
					del kht[-1]
				
				all_interkeyTime.append(ikt)
				all_keyHoldTime.append(kht)
				fig = int('{}{}'.format(user, text))
				plt.figure(fig)
				plt.plot([i/10000 for i in kht], [i/10000 for i in ikt])
		
			plt.xlabel('Key Hold Time (*10^4)(sec)')
			plt.ylabel('Interkey Time (*10^4)(sec)')
			plt.savefig('user{}-text{}.png'.format(user, text))

if __name__ == '__main__':
	plotOfBoxplots()
	profilePlot()
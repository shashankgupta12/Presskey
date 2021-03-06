import statistics
from calculatetimings import calculateKeyHoldTime, calculateInterkeyTime
import json
from outlierdeletion import getPositionOfOutliers

def produceMasterProfileFAR(text, user):
	all_keyHoldTime = []
	all_interkeyTime = []
	
	filename = 'processedData/text{0}/user{1}.json'.format(text, user)
	with open(filename, 'r') as f:
		data = [json.loads(line) for line in f]

	outliers = getPositionOfOutliers(text,user)
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
		
	master_interkeyTime = [statistics.mean(time) for time in zip(*all_interkeyTime)]
	master_keyHoldTime = [statistics.mean(time) for time in zip(*all_keyHoldTime)]
	return (master_interkeyTime, master_keyHoldTime, all_interkeyTime, all_keyHoldTime)

def calculateTrajectoryDissimilaritiesFAR(text, user):
	dissimilarityValues = []
	master_interkeyTime, master_keyHoldTime, all_interkeyTime, all_keyHoldTime = produceMasterProfileFAR(text, user)
	
	for ikt, kht in zip(all_interkeyTime, all_keyHoldTime):
		euclideanDistance = [((x1 - x2)**2 + (y1 - y2)**2)**(1/2) for x1, y1, x2, y2 in zip(master_interkeyTime, master_keyHoldTime, ikt, kht)]
		dissimilarityValues.append(sum(euclideanDistance))

	return dissimilarityValues

def generateComparatorFAR(text, user):
	dissimilarityValues = calculateTrajectoryDissimilaritiesFAR(text, user)
	mean = statistics.mean(dissimilarityValues)
	stdev = statistics.stdev(dissimilarityValues)
	SIGMA = 1.0
	return (mean + (SIGMA * stdev))

if __name__ == '__main__':
	
	import pylab 
	import scipy.stats as stats

	dissimilarity = calculateTrajectoryDissimilaritiesFAR(1, 3)
	dissimilarity = [i/10000 for i in dissimilarity]
	stats.probplot(dissimilarity, dist="norm", plot=pylab)
	pylab.ylabel('Observation quantiles (*10^4)')
	pylab.title('')
	pylab.show()
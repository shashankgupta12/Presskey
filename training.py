import statistics
from calculatetimings import calculateKeyHoldTime, calculateInterkeyTime
import json
import matplotlib.pyplot as plt
from outlierdeletion import getPositionOfOutliers

def produceMasterProfile(text, user, num):
	all_keyHoldTime = []
	all_interkeyTime = []
	filename = 'processedData/text{0}/user{1}.json'.format(text, user)
	with open(filename, 'r') as f:
		data = [json.loads(line) for line in f]
	# for timings in data[:num]:
	outliers = getPositionOfOutliers(text,user)
	for i, timings in enumerate(data):
		if i not in outliers:
		# ct = calculateCumulativeTime(timings['keyPressData'], timings['keyReleaseData'])
			ikt = calculateInterkeyTime(timings['keyPressData'], timings['keyReleaseData'])
			kht = calculateKeyHoldTime(timings['keyPressData'], timings['keyReleaseData'])
			if len(ikt) > len(kht):
				del ikt[-1]
			elif len(kht) > len(ikt):
				del kht[-1]
			all_interkeyTime.append(ikt)
			all_keyHoldTime.append(kht)
		# print(i, ikt)
		# print(lt)
		# plt.figure(1)
		# plt.plot(ikt, lt)
		# all_cumulativeTime.append(ct)
		# break

	# plt.show()
	# plt.savefig('foo.png')
	master_cumulativeTime = [statistics.mean(time) for time in zip(*all_interkeyTime)]
	master_latencyTime = [statistics.mean(time) for time in zip(*all_keyHoldTime)]
	return (master_cumulativeTime, master_latencyTime, all_interkeyTime, all_keyHoldTime)

def calculateTrajectoryDissimilarities(text, user, num):
	dissimilarityValues = []
	master_cumulativeTime, master_latencyTime, all_cumulativeTime, all_latencyTime = produceMasterProfile(text, user, num)
	for ct, lt in zip(all_cumulativeTime, all_latencyTime):
		euclideanDistance = [((x1 - x2)**2 + (y1 - y2)**2)**(1/2) for x1, y1, x2, y2 in zip(master_cumulativeTime, master_latencyTime, ct, lt)]
		dissimilarityValues.append(sum(euclideanDistance))

	return dissimilarityValues

def generateComparator(text, user, num):
	dissimilarityValues = calculateTrajectoryDissimilarities(text, user, num)
	mean = statistics.mean(dissimilarityValues)
	stdev = statistics.stdev(dissimilarityValues)
	SIGMA = 0.0
	return (mean + (SIGMA * stdev))

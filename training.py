import statistics
from calculatetimings import calculateCumulativeTime, calculateLatencyTime, calculateInterkeyTime
import json
import matplotlib.pyplot as plt


def produceMasterProfile(text, user, num):
	all_cumulativeTime = []
	all_latencyTime = []
	filename = 'processedData/text{0}/user{1}.json'.format(text, user)
	with open(filename, 'r') as f:
		data = [json.loads(line) for line in f]
	for timings in data[:num]:
		# ct = calculateCumulativeTime(timings['keyPressData'], timings['keyReleaseData'])
		ct = calculateInterkeyTime(timings['keyPressData'], timings['keyReleaseData'])
		lt = calculateLatencyTime(timings['keyPressData'], timings['keyReleaseData'])
		del ct[-1]
		all_cumulativeTime.append(ct)
		all_latencyTime.append(lt)

	master_cumulativeTime = [statistics.mean(time) for time in zip(*all_cumulativeTime)]
	master_latencyTime = [statistics.mean(time) for time in zip(*all_latencyTime)]
	return (master_cumulativeTime, master_latencyTime, all_cumulativeTime, all_latencyTime)

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
	SIGMA = 1.00
	return (mean + (SIGMA * stdev))
import statistics
from calculatetimings import calculateCumulativeTime, calculateLatencyTime
import json
import matplotlib.pyplot as plt

all_cumulativeTime = []
all_latencyTime = []

def produceMasterProfile():
	with open('data.json', 'r') as f:
		data = json.load(f)
	for timings in data:
		ct = calculateCumulativeTime(timings['keyPressData'], timings['keyReleaseData'])
		lt = calculateLatencyTime(timings['keyPressData'], timings['keyReleaseData'])
		print(ct)
		del ct[-1]
		all_cumulativeTime.append(ct)
		all_latencyTime.append(lt)

	master_cumulativeTime = [statistics.mean(time) for time in zip(*all_cumulativeTime)]
	master_latencyTime = [statistics.mean(time) for time in zip(*all_latencyTime)]
	print(master_cumulativeTime)
	print(master_latencyTime)
	plt.figure(1)
	plt.plot(master_cumulativeTime, master_latencyTime)
	plt.show()
	return (master_cumulativeTime, master_latencyTime)

def calculateTrajectoryDissimilarities():
	dissimilarityValues = []
	master_cumulativeTime, master_latencyTime = produceMasterProfile()
	for ct, lt in zip(all_cumulativeTime, all_latencyTime):
		euclideanDistance = [((x1 - x2)**2 + (y1 - y2)**2)**(1/2) for x1, y1, x2, y2 in zip(master_cumulativeTime, master_latencyTime, ct, lt)]
		dissimilarityValues.append(sum(euclideanDistance))
		plt.figure(1)
		plt.plot(ct, lt)

	plt.savefig("plot.png")
	return dissimilarityValues

def generateComparator():
	dissimilarityValues = calculateTrajectoryDissimilarities()
	# print(dissimilarityValues)
	mean = statistics.mean(dissimilarityValues)
	stdev = statistics.stdev(dissimilarityValues)
	SIGMA = 3.00
	# print(mean, stdev)
	return (mean + (SIGMA * stdev))

# print(generateComparator())
# print(calculateTrajectoryDissimilarities())
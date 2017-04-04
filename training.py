import statistics
from calculatetimings import calculateCumulativeTime, calculateLatencyTime, calculateInterkeyTime
import json
import matplotlib.pyplot as plt


def produceMasterProfile(text, user, num):
	# all_cumulativeTime = []
	all_latencyTime = []
	all_interkeyTime = []
	all_cumulativeTime = []
	filename = 'processedData/text{0}/user{1}.json'.format(text, user)
	with open(filename, 'r') as f:
		data = [json.loads(line) for line in f]
	# for timings in data[:num]:
	for i, timings in enumerate(data):
		# ct = calculateCumulativeTime(timings['keyPressData'], timings['keyReleaseData'])
		ikt = calculateInterkeyTime(timings['keyPressData'], timings['keyReleaseData'])
		lt = calculateLatencyTime(timings['keyPressData'], timings['keyReleaseData'])
		if len(ikt) > len(lt):
			del ikt[-1]
		elif len(lt) > len(ikt):
			del lt[-1]
		all_interkeyTime.append(ikt)
		all_latencyTime.append(lt)
		# print(i, ikt)
		# print(lt)
		# plt.figure(1)
		# plt.plot(ikt, lt)
		# all_cumulativeTime.append(ct)
		# break

	# plt.show()
	# plt.savefig('foo.png')
	master_cumulativeTime = [statistics.mean(time) for time in zip(*all_interkeyTime)]
	master_latencyTime = [statistics.mean(time) for time in zip(*all_latencyTime)]
	return (master_cumulativeTime, master_latencyTime, all_interkeyTime, all_latencyTime)

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
	return (dissimilarityValues ,mean, stdev)
	# SIGMA = 1.00
	# return (mean + (SIGMA * stdev))

if __name__ == '__main__':
	d, a, s = generateComparator(1, 7, 40)
	# print(sum(d)/len(d))
	# for i in d:
	# 	print('{0}  {1}  {2}  {7}'.format(a,i,s,a+s-i))
	# print(a)
	# print(1 / (1 + a))
	# a = 1 / (1 + a)
	# s = 1 / (1 + s)
	# print(a)
	# print(s)
	a = 1 / (1 + a)
	s = 1 / (1 + s)
	count = 0
	allUserCount = 0
	master_ct, master_lt, c, d = produceMasterProfile(1, 7, 40)
	# userlist = [u for u in range(1, 12) if not u == 1]
	userlist = [u for u in range(1, 12)]
	print(userlist)
	for user in userlist:
		print(user)
		filename = 'processedData/text1/user{0}.json'.format(user)
		with open(filename, 'r') as f:
			data = [json.loads(line) for line in f]
		for timings in data:
			# ct = calculateCumulativeTime(timings['keyPressData'], timings['keyReleaseData'])
			ct = calculateInterkeyTime(timings['keyPressData'], timings['keyReleaseData'])
			lt = calculateLatencyTime(timings['keyPressData'], timings['keyReleaseData'])
			
			euclideanDistance = [((x1 - x2)**2 + (y1 - y2)**2)**(1/2) for x1, y1, x2, y2 in zip(master_ct, master_lt, ct, lt)]
			dissimilarity = sum(euclideanDistance)
			b = 1 / (1 + dissimilarity)
			l = 'imposter' if b < (a) else 'legitimate'
			if l == 'legitimate':
				count += 1
			allUserCount += 1
			print(l)

		print()
	print((count/allUserCount)*100)
			# authenticationValue = 1 if dissimilarity <= comparator else 0
			# user = 'Legitimate' if authenticationValue == 1 else 'Imposter'
	# print(len(a[0]))
	# print(len(a[1]))
	# print(len(a[2]))
	# print(len(a[3]))
from calculatetimings import calculateInterkeyTime
import matplotlib.pyplot as plt

def plot():
	filename = 'processedData/text{0}/user{1}.json'.format(1, 8)
	with open(filename, 'r') as f:
		data = [json.loads(line) for line in f]
	all_ikt = [[i/10000 for i in calculateInterkeyTime(timings['keyPressData'], timings['keyReleaseData'])] for timings in data]
	ikt = [list(lst) for lst in zip(*all_ikt)]
	plt.figure()
	plt.boxplot(ikt, vert=0)
	my_yticks = ['a-b', 'b-u', 'u-Shift', 'Shift-@', '@-9', '9-,', ',-l', 'l-1', '1-2', '2-Shift', 'Shift-$']
	plt.yticks(list(range(1, 12)), my_yticks)
	plt.xlabel('Range of interkey values')
	plt.ylabel('Box plots')
	plt.show()
	# plt.savefig('foo.png')

def produce(text, user):
	all_keyHoldTime = []
	all_interkeyTime = []
	filename = 'processedData/text{0}/user{1}.json'.format(text, user)
	with open(filename, 'r') as f:
		data = [json.loads(line) for line in f]
	outliers = getPositionOfOutliers(text,user)
	for i, timings in enumerate(data):
		if i not in outliers:
			ikt = calculateInterkeyTime(timings['keyPressData'], timings['keyReleaseData'])
			kht = calculateKeyHoldTime(timings['keyPressData'], timings['keyReleaseData'])
			if len(ikt) > len(kht):
				del ikt[-1]
			elif len(kht) > len(ikt):
				del kht[-1]
			all_interkeyTime.append(ikt)
			all_keyHoldTime.append(kht)
			print(ikt)
			print(kht)
			plt.figure(1)
			plt.plot([i/10000 for i in kht], [i/10000 for i in ikt])
	plt.xlabel('Key Hold Time (*10^4)(sec)')
	plt.ylabel('Interkey Time (*10^4)(sec)')
	plt.show()
	# plt.savefig('foo.png')

def produce1(text, user):
	all_keyHoldTime = []
	all_interkeyTime = []
	filename = 'processedData/text{0}/user{1}.json'.format(text, user)
	with open(filename, 'r') as f:
		data = [json.loads(line) for line in f]
	outliers = getPositionOfOutliers(text,user)
	for i, timings in enumerate(data):
		ikt = calculateInterkeyTime(timings['keyPressData'], timings['keyReleaseData'])
		kht = calculateKeyHoldTime(timings['keyPressData'], timings['keyReleaseData'])
		if len(ikt) > len(kht):
			del ikt[-1]
		elif len(kht) > len(ikt):
			del kht[-1]
		all_interkeyTime.append(ikt)
		all_keyHoldTime.append(kht)
		print(ikt)
		print(kht)
		plt.figure(1)
		plt.plot([i/10000 for i in kht], [i/10000 for i in ikt])
	plt.xlabel('Key Hold Time (*10^4)(sec)')
	plt.ylabel('Interkey Time (*10^4)(sec)')
	plt.show()
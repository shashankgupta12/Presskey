from training import produceMasterProfile
import json
from calculatetimings import calculateKeyHoldTime, calculateInterkeyTime

def authenticate(user, text, num, comparator):
	master_ct, master_lt, c, d = produceMasterProfile(text, user, num)
	userlist = [u for u in range(1, 12) if not u == user]
	count = 0
	allUserCount = 0 
	for user in userlist:
		filename = 'processedData/text{0}/user{1}.json'.format(text, user)
		with open(filename, 'r') as f:
			data = [json.loads(line) for line in f]
		for timings in data:
			# ct = calculateCumulativeTime(timings['keyPressData'], timings['keyReleaseData'])
			ct = calculateInterkeyTime(timings['keyPressData'], timings['keyReleaseData'])
			lt = calculateKeyHoldTime(timings['keyPressData'], timings['keyReleaseData'])
			del ct[-1]
			euclideanDistance = [((x1 - x2)**2 + (y1 - y2)**2)**(1/2) for x1, y1, x2, y2 in zip(master_ct, master_lt, ct, lt)]
			dissimilarity = sum(euclideanDistance)
			authenticationValue = 1 if dissimilarity <= comparator else 0
			user = 'Legitimate' if authenticationValue == 1 else 'Imposter'
			if user == 'Legitimate':
				count += 1
			allUserCount += 1
	return ((count / allUserCount) * 100)


def simcalc(user, text):
	master_ikt, master_lt, c, d = produceMasterProfile(text, user, 40)
	userlist = [u for u in range(1, 12) if not u == user]
	sim = []
	for user in userlist:
		master_ik, master_l, c, d = produceMasterProfile(text, user, 40)
		euclideanDistance = [((x1 - x2)**2 + (y1 - y2)**2)**(1/2) for x1, y1, x2, y2 in zip(master_ikt, master_lt, master_ik, master_l)]
		dissimilarity = sum(euclideanDistance)
		simi = dissimilarity/10**6
		sim.append((1 /(1 + simi))*100)
	return sim
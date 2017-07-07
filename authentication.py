from trainingFAR import produceMasterProfileFAR
from trainingFRR import produceMasterProfileFRR
import json
from calculatetimings import calculateKeyHoldTime, calculateInterkeyTime
from outlierdeletion import getPositionOfOutliers

def authenticateFAR(user, text, comparator):
	master_ikt, master_kht, c, d = produceMasterProfileFAR(text, user)
	userlist = [u for u in range(1, 12) if not u == user]
	count = 0
	allUserCount = 0 
	
	for user in userlist:
		filename = 'processedData/text{0}/user{1}.json'.format(text, user)
		with open(filename, 'r') as f:
			data = [json.loads(line) for line in f]
		
		outliers = getPositionOfOutliers(text,user)
		data = [timings for i, timings in enumerate(data) if not i in outliers]
		
		for timings in data:
			ikt = calculateInterkeyTime(timings['keyPressData'], timings['keyReleaseData'])
			kht = calculateKeyHoldTime(timings['keyPressData'], timings['keyReleaseData'])
			
			if len(ikt) > len(kht):
				del ikt[-1]
			elif len(kht) > len(ikt):
				del kht[-1]
			
			euclideanDistance = [((x1 - x2)**2 + (y1 - y2)**2)**(1/2) for x1, y1, x2, y2 in zip(master_ikt, master_kht, ikt, kht)]
			dissimilarity = sum(euclideanDistance)
			authenticationValue = 1 if dissimilarity <= comparator else 0
			user = 'Legitimate' if authenticationValue == 1 else 'Imposter'
			if user == 'Legitimate':
				count += 1
			allUserCount += 1
	
	return ((count / allUserCount) * 100)

def authenticateFRR(user, text, comparator):
	master_ikt, master_kht, c, d = produceMasterProfileFRR(text, user)
	count = 0
	allUserCount = 0 
	filename = 'processedData/text{0}/user{1}.json'.format(text, user)
	
	with open(filename, 'r') as f:
		data = [json.loads(line) for line in f]
	
	outliers = getPositionOfOutliers(text,user)
	data = [timings for i, timings in enumerate(data) if not i in outliers]
	
	for timings in data[5:]:
		ikt = calculateInterkeyTime(timings['keyPressData'], timings['keyReleaseData'])
		kht = calculateKeyHoldTime(timings['keyPressData'], timings['keyReleaseData'])

		if len(ikt) > len(kht):
			del ikt[-1]
		elif len(kht) > len(ikt):
			del kht[-1]

		euclideanDistance = [((x1 - x2)**2 + (y1 - y2)**2)**(1/2) for x1, y1, x2, y2 in zip(master_ikt, master_kht, ikt, kht)]
		dissimilarity = sum(euclideanDistance)
		authenticationValue = 1 if dissimilarity <= comparator else 0
		user = 'Legitimate' if authenticationValue == 1 else 'Imposter'
		if user == 'Imposter':
			count += 1
		allUserCount += 1
	
	return ((count / allUserCount) * 100)
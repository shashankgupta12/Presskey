from pynput.keyboard import Key, Listener
from datetime import datetime
from dataprocess import dataProcess, extractTimings
from calculatetimings import calculateCumulativeTime, calculateLatencyTime
from training import generateComparator, produceMasterProfile

pressdata = []
releasedata = []

def authenticate():
	dp, dr = extractTimings(dataProcess(pressdata), dataProcess(releasedata))
	ct = calculateCumulativeTime(dp, dr)
	lt = calculateLatencyTime(dp, dr)
	# master_lt = []
	# master_ikt = []
	master_ct, master_lt = produceMasterProfile()


	euclideanDistance = [((x1 - x2)**2 + (y1 - y2)**2)**(1/2) for x1, y1, x2, y2 in zip(master_ct, master_lt, ct, lt)]
	dissimilarity = sum(euclideanDistance)
	comparator = generateComparator()
	authenticationValue = 1 if dissimilarity <= comparator else 0
	# print(authenticationValue)
	user = 'Legitimate' if authenticationValue == 1 else 'Imposter'
	print(user)

def onPress(key):
	t = datetime.now()
	if not key == Key.enter:
		time = t.minute*60*(10**6) + t.second*(10**6) + t.microsecond
		pressdata.append("p-{0}-{1}".format(key,time))

def onRelease(key):
	t = datetime.now()
	if key == Key.enter:
		return False
	else:
		time = t.minute*60*(10**6) + t.second*(10**6) + t.microsecond
		releasedata.append("r-{0}-{1}".format(key,time))

def userInput():
	text = 'shashank'
	print("Type the following text: {0}".format(text))
	with Listener(on_press=onPress, on_release=onRelease) as listener:
		listener.join()
	authenticate()

userInput()
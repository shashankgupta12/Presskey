def calculateKeyHoldTime(keyPressData, keyReleaseData):
    return [t2 - t1 for (t1, t2) in zip(keyPressData, keyReleaseData)]
    
def calculateLatencyTime(keyPressData, keyReleaseData):
    return [t2 - t1 for (t1, t2) in zip(keyPressData[:-1], keyPressData[1:])]
    
def calculateInterkeyTime(keyPressData, keyReleaseData):
    return [t2 - t1 for (t1, t2) in zip(keyReleaseData[:-1], keyPressData[1:])]

def calculateCumulativeTime(keyPressData, keyReleaseData):
	return [t1 - keyPressData[0] for t1 in keyReleaseData]
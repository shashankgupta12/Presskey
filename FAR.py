from trainingFAR import generateComparatorFAR
from trainingFRR import generateComparatorFRR
from authentication import authenticateFAR, authenticateFRR
import statistics

def calculateFAR():
	FARs = []
	for text in range(1, 5):
		textWiseFAR = []
		for user in range(1, 12):
			comp = generateComparator(text, user)
			FAR = authenticateFAR(user, text, comp)
			print('user{0}: {1}'.format(user, FAR))
			textWiseFAR.append(FAR)
		far = statistics.mean(textWiseFAR)
		print(far)
		FARs.append(far)
		print()
	print(FARs)

def calculateFRR():
	FRRs = []
	for text in range(1, 5):
		textWiseFRR = []
		for user in range(1, 12):
			comp = generateComparator(text, user)
			FRR = authenticateFRR(user, text, comp)
			print('user{0}: {1}'.format(user, FRR))
			textWiseFRR.append(FRR)
		frr = statistics.mean(textWiseFRR)
		print(frr)
		FRRs.append(frr)
		print()
	print(FRRs)

if __name__ == '__main__':
	calculateFAR()
	calculateFRR()
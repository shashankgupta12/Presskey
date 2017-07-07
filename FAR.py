from training import generateComparator
from authentication import authenticateFAR, authenticateFRR
import statistics

def calculateFAR():
	FARs = []
	for text in range(1, 5):
		textWiseFAR = []
		for user in range(1, 12):
			comp = generateComparator(text, user, 40)
			FAR = authenticateFAR(user, text, 40, comp)
			print('user{0}: {1}'.format(user, FAR))
			textWiseFAR.append(FAR)
		FARs.append(statistics.mean(textWiseFAR))
		print()
	print(FARs)

def calculateFRR():
	FRRs = []
	for text in range(1, 5):
		textWiseFRR = []
		for user in range(1, 12):
			comp = generateComparator(text, user, 40)
			FRR = authenticateFRR(user, text, 40, comp)
			print('user{0}: {1}'.format(user, FRR))
			textWiseFRR.append(FRR)
		FRRs.append(statistics.mean(textWiseFRR))
		print()
	print(FRRs)

if __name__ == '__main__':
	calculateFAR()
	# calculateFRR()
from training import generateComparator
from authentication import authenticate, simcalc
import statistics
import numpy as np
import matplotlib.pyplot as plt

def barPlot(FAR):
	for far in FAR:
		objects = ('String1', 'String2', 'String3', 'String4')
		y_pos = np.arange(len(objects))
		 
		plt.bar(y_pos, far, align='center', alpha=0.5)
		plt.xticks(y_pos, objects)
		plt.ylabel('FAR')
		plt.title('Types of strings used')
		figname = 'foo{0}.png'.format(far)
		plt.savefig(figname)

def calculateFAR():
	FARs = []
	for text in range(1, 2):
		textWiseFAR = []
		# print('text{0}'.format(text))
		# userWiseFAR = []
		for user in range(1, 12):
			# for profile in [10, 15, 20, 30]:
			comp = generateComparator(text, user, 40)
			FAR = authenticate(user, text, 40, comp)
			# userWiseFAR.append(FAR)
			textWiseFAR.append(FAR)
			print('user{0}: {1}'.format(user, FAR))
		FARs.append([statistics.mean(textWiseFAR)])
		print()
	# barPlot(FARs)
	print(FARs)

def calculateSimilarity():
	for user in range(1,12):
		sim = simcalc(user, 1)
		print(user)
		for i,j in enumerate(sim):
			print('User_: {0}'.format(j/11))

# calculateSimilarity()
calculateFAR()
from training import generateComparator
from authentication import authenticate
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
	for text in range(1, 5):
		textWiseFAR = []
		# print('text{0}'.format(text))
		for user in range(1, 12):
			userWiseFAR = []
			for profile in [10, 15, 20, 30]:
				comp = generateComparator(text, user, profile)
				FAR = authenticate(user, text, profile, comp)
				userWiseFAR.append(FAR)
				print('user{0}:profile{1}:{2}'.format(user, profile, FAR), end=' ')
			textWiseFAR.append(userWiseFAR)
			print()
		FARs.append([statistics.mean(far) for far in zip(*textWiseFAR)])
		print()
	barPlot(FARs)
	print(FARs)

calculateFAR()
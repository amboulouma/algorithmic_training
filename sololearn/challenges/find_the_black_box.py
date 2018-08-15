# Challenge Find the black box
# Author Amine M Boulouma
# 23/03/2018
import random
boxes = [x for x in range(10, 21)]*10
boxes[random.randint(0, 100)] = 21
boxes[random.randint(0, 100)] = 9
for i in boxes:
	if i < 10 or i > 20:
		print(i)
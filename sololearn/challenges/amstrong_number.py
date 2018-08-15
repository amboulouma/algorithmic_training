# Challenge Amstrong number
# Author Amine M Boulouma
# 23/03/2018

def isAmstrong(num):
	sum = 0
	for i in str(num):
		sum += int(i)**3
	return (sum == num)
	
print(isAmstrong(int(input())))
for i in range(int(input())):
	if isAmstrong(i):
		print(i)
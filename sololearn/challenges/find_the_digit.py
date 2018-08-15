# Challenge Find the digit
# Author Amine M Boulouma
# 23/03/2018
n, d = map(int, input().split(' '))
for i in map(str, range(n)):
	if str(d) in i:
		print(int(i))
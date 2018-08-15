# Challenge perfect number
# Author Amine M Boulouma
# 23/03/2018
n = int(input())
s = 0
for i in range(1, n):
	if not n%i:
		s += i
print(s == n)
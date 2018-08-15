# Challenge Abundant Number
n = int(input())
s=0
for i in range(1, n +1):
	if not n%i:
		s += i
if s >= 2*n:
	print("abundant")
else:
	print("not abundant")
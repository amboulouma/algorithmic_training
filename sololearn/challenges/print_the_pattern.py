# Challenge Print the pattern
n = int(input())
for i in range(1, n+1):
	for j in range(i):
		print(i, end='')
	print()
for i in range(1, n+1):
	for j in range(1, i+1):
		print(j, end='')
	print()
for i in range(1, n+1):
	for j in range(2*i):
		if j%2:
			print(j, end='')
	print()
for i in range(n+1):
	for j in range(i):
		print(j%2, end='')
	print()
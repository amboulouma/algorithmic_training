# Challenge Reciprocal Letter
alphabet = [x for x in map(chr, range(ord('a'), ord('z') + 1))]
alphabetC = [x for x in map(chr, range(ord('A'), ord('Z') + 1))]

reverse = alphabet[::-1]
reverseC = alphabetC[::-1]

for i in input():
	if i in alphabet:
		print(reverse[alphabet.index(i)], end='')
	elif i in alphabetC:
		print(reverseC[alphabetC.index(i)], end='')
	else:
		print(i, end='')
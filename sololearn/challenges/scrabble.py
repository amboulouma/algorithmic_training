# Challenge Scrabble

alpha=list("abcdefghijklmnopqrstuvwxyz")
points="1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10".split(",")
scores = {}
for word in input().split(' '):
	scores[word] = 0
	for letter in word:
		scores[word] += int(points[alpha.index(letter)])
print(max(scores, key = scores.get))
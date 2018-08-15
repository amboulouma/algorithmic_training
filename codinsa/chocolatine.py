n = int(input())
sums = [0]
for i in range(n):
    temp = list(map(int, str(input()).split()))
    tempSums = []
    k = 0
    for j in range(len(temp)):
        if (j+1) % 3 == 0:
            k += 1
            j -= 1
            tempSums.append(sums[k] + temp[j])
            j += 1
        tempSums.append(sums[k] + temp[j])
    sums = tempSums
print(max(sums))

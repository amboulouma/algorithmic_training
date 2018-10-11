numbers = list(map(int, input().split()))
times_unlucky = len([i for i in numbers if i == 13])
print(times_unlucky)
for i in range(times_unlucky):
    index_unlucky = numbers.index(13)
    if index_unlucky != len(numbers)-1:
        del numbers[index_unlucky+1]
    del numbers[index_unlucky]
print(sum(numbers))

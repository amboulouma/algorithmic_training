def recursive_num_ways(n):
    if n == 0 or n == 1:
        return 1
    else:
        return recursive_num_ways(n-1) + recursive_num_ways(n-2)


def optimized_num_ways(n):
    nums = [0]*(n+1)
    nums[0] = 1
    nums[1] = 1
    if n >= 2:
        for i in range(2, n+1):
            nums[i] = nums[i-1] + nums[i-2]
    return nums[n]


print(recursive_num_ways(2))
print(recursive_num_ways(3))
print(recursive_num_ways(4))

print(optimized_num_ways(2))
print(optimized_num_ways(3))
print(optimized_num_ways(4))

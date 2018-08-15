def can_balance(array):
    for i in range(len(array)):
        if sum(array[:i]) == sum(array[i:]):
            return True
    return False

print(can_balance([10, 10]))
def sum_numbers(str):
    numbers = ''
    for c in str:
        if c.isdigit():
            numbers += c
        else:
            numbers += ' '
    numbers_list = numbers.split(' ')
    spaces = range(numbers_list.count(''))
    for i in spaces:
        numbers_list.remove('')
    return sum(list(map(int, numbers_list)))

print(sum_numbers("7 11"))
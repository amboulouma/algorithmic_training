sorted_array = []
def sorting_array(array):
    if array != []:
        array = list(set(array))
        sorted_array.append(min(array))
        array.remove(min(array))
        sorting_array(array)
    else:
        return

sorting_array([2,1,2,1,2,1,2,1,2,1,2,1,9,10,22,45,3])
print(sorted_array)
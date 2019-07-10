def find_max(numbers, index):
    if len(numbers)==0:
        return 0
    if len(numbers)==1:
        return numbers[0]
    else:
        if find_max(numbers[:-1], index-1)>= numbers[index]:
            return find_max(numbers[:-1], index-1)
        if find_max(numbers[:-1], index-1) < numbers[index]:
            return numbers[index]

# index= len(numbers)-1

assert(find_max([1, 2, 3], 2) == 3)
print(find_max([1, 2, 3], 2))
assert(find_max([100, 2, 100], 2) == 100)
print(find_max([100, 2, 100], 2))
assert(find_max([], 0) == 0) # what is your return value for empty list?
assert(find_max([11], 1) == 11)
assert(find_max([11, 0], 1) == 11)
assert(find_max([11, -19], 1) == 11)



"""
def max_num(numbers):
    length= len(numbers)
    if length==0:
        return 0
    elif length==1:
        return numbers[0]
    elif numbers[0] >= numbers[1]:
        del numbers[1]
    elif numbers[0] < numbers[1]:
        del numbers[0]
    return max_num(numbers)

print(max_num([1,2,3,4]))
"""
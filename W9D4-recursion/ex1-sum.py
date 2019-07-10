def my_sum(numbers, index):
    if len(numbers)==0:
        return 0
    elif index == len(numbers)-1:
        return numbers[index]
    return my_sum(numbers, index +1) +numbers[index]

assert(my_sum([1, 2, 3, 4, 5], 3) == 9)
print(my_sum([1, 2, 3, 4, 5], 3))
assert(my_sum([1, 2, 3, 4, 5], 0) == 15)
print(my_sum([1, 2, 3, 4, 5], 0))
assert(my_sum([], 0) == 0)
print(my_sum([], 0))
assert(my_sum([11], 0) == 11)
print(my_sum([11], 0))
assert(my_sum([11, 0], 0) == 11)
print(my_sum([11, 0], 0))
assert(my_sum([11, -1], 0) == 10)
print(my_sum([11, -1], 0))
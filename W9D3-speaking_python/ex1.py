def summing(list_num):
    sum = 0
    for element in list_num:
        if type(element)== int or type(element)== float:
            sum += element
    print(sum)
    return sum

summing(["ar",2,3,1.5])
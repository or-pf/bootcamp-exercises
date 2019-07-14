def intersection(list1, list2):
    new_list=[]
    
    for a in list1:
         for b in list2:
             if a == b :
                new_list.append(a)
    return new_list

print(intersection([1,2,3], [2,4,3,5,6,6,6]))
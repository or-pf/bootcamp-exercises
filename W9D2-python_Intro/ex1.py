for i in range (1,41): 
    print (i)



i=1
while i < 41:
    print(i)
    i += 1

my_list= list(range(1,101))
for num in my_list:
    if num % 15 == 0:
        print ("fizzbuzz")
    elif num % 5 == 0:
        print ("buzz")
    elif num % 3 == 0 :
        print ("fizz")
    else :
        print(num)
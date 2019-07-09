number= input("please enter a 5 digit number")
print(f"you entered the number {number}")

#print (f"the digits of the number are {number[0]}, {number[1]}, {number[2]}, {number[3]}, {number[4]}") 
sum=0
print (f"the digits of the number are " , end="")
for digit in number:
    print (digit, end=",")
    sum += int(digit)
print (f"the sum of the digits is: {sum}")



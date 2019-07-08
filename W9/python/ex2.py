number= input("please enter a 5 digit number")
print(f"you entered the number {number}")

print (f" the digits of the number are {number[0]}, {number[1]}, {number[2]}, {number[3]}, {number[4]}") 
for place in number:
    digit= int(place)
    sum += digit
print (f"the sum of the digits is: {sum}")



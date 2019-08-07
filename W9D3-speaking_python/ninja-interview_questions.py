# Very simple exercises
# 1.Define a function max() that takes two numbers as arguments and returns the largest of them. Use the if-then-else construct available in Python. (It is true that Python has the max() function built in, but writing it yourself is nevertheless a good exercise.)
def maxi (x,y):
    if x > y:
        return x, print(x)
    else:
        return y, print(y)
maxi(1,4)
maxi(60,14)

# 2.Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.
def max_of_three(x,y,z):
    print (max(x,y,z))
    return max(x,y,z) 

max_of_three(1,30,78)

print ("enter three numbers with spaces beetween each one")
full_string=input()
list_of_numbers_as_str= full_string.split()
list_of_integers=[]
for num in list_of_numbers_as_str:
    list_of_integers.append(int(num))

def max_of_three(list):
    if list[0]>list[1]:
        if list[0]>list[2]:
            print (str(list[0])+" is largest")
        else: 
            print (str(list[2])+" is largest")

    else:
        if list[1]>list[2]:
            print (str(list[1])+" is largest")
        else:
            print (str(list[2])+" is largest")

max_of_three(list_of_integers)

# 3.Define a function that computes the length of a given list or string. (It is true that Python has the len() function built in, but writing it yourself is nevertheless a good exercise.)
print("enter a string")
full_string=input()
def count_length(full_string):
    counter = 0
    if full_string[0]== "[":
        list_from_str = full_string.split(", ")
        for num in list_from_str:
            counter += 1
    else:
        for i in full_string:
            counter += 1
    print (str(counter))

count_length(full_string)
# check:
count_length([1, 3, 5, 6])

# 4.Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.
vowels_list =["a","e","i","u","o"]
def is_vowel(char):
    if char in vowels_list:
        print (char + " is a vowel")
        return True
    else:
        print (char +" is not a vowel")
        return False

is_vowel("b")
is_vowel("u")

# 5.Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber's language"). That is, double every consonant and place an occurrence of "o" in between. For example, translate("this is fun") should return the string "tothohisos isos fofunon".
print("enter a string")
my_string=input()

def translate(stringi):
    translated_string=""
    for i in stringi:
        if i not in vowels_list and i !=" ":
            translated_string += i+"o"+i
        else:
            translated_string +=i
    print(translated_string)

translate(my_string)

# 6.Define a function sum() and a function multiply() that sums and multiplies (respectively) all the numbers in a list of numbers. For example, sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24.

print ("enter a list of numbers with a space between each number")
full_string=input()
list_of_numbers_as_str= full_string.split()
def sum(list_of_numbers_as_str):
    sum_of_integers=0
    for num in list_of_numbers_as_str:
        sum_of_integers += (int(num))
    print(sum_of_integers)

def multiply(list_of_numbers_as_str):
    multiplication=1
    for num in list_of_numbers_as_str:
        multiplication *= (int(num))
    print(multiplication)

sum(list_of_numbers_as_str)
multiply(list_of_numbers_as_str)

# # 7.Define a function reverse() that computes the reversal of a string. For example, reverse("I am testing") should return the string "gnitset ma I".
def reverse(stringi):
    reversed_stringi = ""
    for i in stringi:
        reversed_stringi += stringi[-1]
        stringi = stringi[:-1]
    print(" the reversed string is: "+reversed_stringi)
    return reversed_stringi

reverse("helo")
reverse("tyg 8bn")
reverse("I am testing")

# 8.Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same written backwards). For example, is_palindrome("radar") should return True.
def is_palindrome(some_str):
    if reverse(some_str) == some_str:
        print(some_str +" is a palindrome")
        return True
    else:
        print(some_str +" is NOT a palindrome")
        return False
is_palindrome("pop")
is_palindrome("pope")
print ("Enter string to check if it's a palindrome")
stringToCheck = input()
is_palindrome(stringToCheck)

# 9.Write a function is_member() that takes a value (i.e. a number, string, etc) x and a list of values a, and returns True if x is a member of a, False otherwise. (Note that this is exactly what the in operator does, but for the sake of the exercise you should pretend Python did not have this operator.)
def is_member(a, list):
    for item in list:
        if item == a:
            return True
    else: 
        return False
if is_member("b", ["w", 5, "y", "g"]):
    print("b is a member")
else:
    print("b is not a member of the list")

# 10.Define a function overlapping() that takes two lists and returns True if they have at least one member in common, False otherwise. You may use your is_member() function, or the in operator, but for the sake of the exercise, you should (also) write it using two nested for-loops.
def overlapping(lista, listb):
    for a in lista:
        for b in listb:
            if a == b:
                print("the lists are overlapping")
                return True
    print("the lists are NOT overlapping")
    return False
                

overlapping(["a", "b", 3], [1, 2 ,5 ,7 ,"u"])
overlapping(["a", "b", 3, 99], ["y", 3, 5])

# 11.Define a function generate_n_chars() that takes an integer n and a character c and returns a string, n characters long, consisting only of c:s. For example, generate_n_chars(5,"x") should return the string "xxxxx". (Python is unusual in that you can actually write an expression 5 * "x" that will evaluate to "xxxxx". For the sake of the exercise you should ignore that the problem can be solved in this manner.)
def generate_n_chars(n, x):
    for i in range (n):
        print ("x" ,end="")
generate_n_chars(5, "t")

# 12.Define a procedure histogram() that takes a list of integers and prints a histogram to the screen. For example, histogram([4, 9, 7]) should print the following:
def histogram(list):
    print ("\n")
    for i in range(len(list)):
            print("*" * list[i])

histogram([2,3,7])
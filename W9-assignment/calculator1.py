import random
num1 =0
num2 =0
operator=""
correct_count=0
wrong_count=0

def create_problem():
    global operator 
    operator = random.choice(["-", "+", "*"])
    global num1
    num1= random.randint(0,9)
    global num2
    num2= random.randint(0,9)  
    return [num1, num2, operator]
    

def get_user_solution():
    create_problem()
    print(num1,operator,num2," = ?")
    ans= int(input())
    return ans

def find_real_solution():   
    solution=""
    if operator == "+":
        solution = num1 + num2
    elif operator == "-":
        solution = num1 - num2
    elif operator == "*":
        solution = num1 * num2
    return solution

def summery():
    print(correct_count," is the amout of correct answers you had")
    print(wrong_count," is the amout of correct answers you had")
    success_percentage= round(correct_count/(correct_count+wrong_count),2)
    print("your overall success rate is :",success_percentage)

def check_solution(ans, solution):

    if ans == solution:
        global correct_count
        correct_count= correct_count+1
        print("Correct.")
        
    else:
        global wrong_count
        wrong_count= wrong_count +1
        print("Incorrect.")

    if correct_count != 0 or wrong_count!= 0:
        print("would you like to continue?")
        will_continue= input()
        if will_continue in ["no", "No", "n", "N" ,""]:
            summery()
        elif will_continue in ["yes", "Yes", "y", "Y","ye","sure","ya"]:
            print("here we go again...")
            create_problem()
            check_solution(get_user_solution(),find_real_solution())


#get_user_solution()
check_solution(get_user_solution(),find_real_solution())

from utilities.numbers_generator import generate_numbers

def add( num1, num2):
    return num1+ num2

def add_generated_numbers():
    num1, num2 = generate_numbers()
    return add(num1,num2)

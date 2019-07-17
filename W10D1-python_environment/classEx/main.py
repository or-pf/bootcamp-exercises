#from calculator import add, add_generated_numbers
# import calculator / can write this instead the line above:
# this would import the entire file- and then can use every function in it
import sys
print(sys.path)

from logic.calculator import add, add_generated_numbers

if __name__ == "__main__":
    print (add(1,2))
    print (add_generated_numbers())
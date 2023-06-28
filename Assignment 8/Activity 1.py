# This program takes iteration input from user and outputs 
# a multiplication table with x(input) number of expressions 
#
# References: 
# https://harpercollege.pressbooks.pub/programmingfundamentals
# /chapter/python-examples-5/
# https://www.w3schools.com/python/python_for_loops.asp


def get_value():
    print("What value would you like to multiply by?")
    value = int(input())
    return value


def get_iteration():
    print("How many expressions would like to run?")
    iterations = int(input())
    return iterations


def demonstrate_for_loop(iterations, value):
    for x in range(1, iterations + 1):
        display_result(value, x)
        x += 1


def display_result(value, x):
    print(f"{value} x {x} = {x*value}")
    return


def main():
    value = get_value()
    iterations = get_iteration()
    demonstrate_for_loop(iterations, value) 


main()

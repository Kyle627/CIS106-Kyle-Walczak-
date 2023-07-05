# This program takes test scores (amount of tests is dependent on user 
# input) and averages the scores. 
#
# References:
# https://harpercollege.pressbooks.pub/programmingfundamentals
# /chapter/python-examples-5/
# https://www.w3schools.com/
# python/python_while_loops.asp


def get_score(): 
    total = 0 
    counter = 0
    while True: 
        print("Enter test score:")
        score = int(input())
        if score < 0:
            break
        total += score
        counter += 1
    return total, counter
 
def calculate_average(total, counter):
    average_score = total / counter
    return average_score


def display_results(average_score):
    print(f"Average Score: {average_score}")
    return


def main():
    total, counter = get_score()
    average_score = calculate_average(total, counter)
    display_results(average_score)


main()

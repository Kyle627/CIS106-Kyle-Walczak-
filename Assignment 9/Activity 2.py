# This program takes test scores (amount of tests is dependent on user 
# input) and averages the scores. 
#
# References:
# https://harpercollege.pressbooks.pub/programmingfundamentals
# /chapter/python-examples-5/
# https://www.w3schools.com/
# python/python_while_loops.asp


def get_count(): 
    print("How many tests scores will you be entering?")
    count = int(input())
    return count


def get_score(count):
    total = 0
    x = count -1 
    while x >= 0:
        print("Enter test score:")
        score = int(input())
        total = total + score
        x -= 1
    return total
    

def calculate_average(total, count):
    average_score = total/count
    return average_score


def display_results(average_score):
    print(f"Average Score: {average_score}")
    return


def main():
    count = get_count()
    total = get_score(count)
    average_score = calculate_average(total,count)
    display_results(average_score)


main()

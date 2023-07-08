# This program takes inputted test scores and sorts from
# highest to lowest
#
# References:
# https://harpercollege.pressbooks.pub/programmingfundamentals
# /chapter/python-examples-6/
# https://www.w3schools.com/python/python_arrays.asp


def get_test_count():
    print("How many tests will you be entering?")
    count = int(input())
    return count


def get_test_scores(count):
    counter = 0
    test_scores = [0] * count
    while counter < count:
        print("Enter test score:")
        test_score = int(input())
        test_scores[counter] = test_score
        counter += 1
    return test_scores
        
        
def sort_scores(test_scores):
    test_scores.sort()
    test_scores.reverse()
    return test_scores


def display_result(test_scores):
    print(f"Sorted scores are: {test_scores}")
    
    
def main():
    count = get_test_count()
    test_scores = get_test_scores(count)
    sort_scores(test_scores)
    display_result(test_scores)


main()

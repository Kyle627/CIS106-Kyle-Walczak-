# This program takes inputted test scores from 0-100 and sorts
# from highest to lowest 
#
# References:
# https://harpercollege.pressbooks.pub/programmingfundamentals
# /chapter/python-examples-6/
# https://www.w3schools.com/python/python_arrays.asp
# https://www.w3schools.com/python/ref_func_input.asp


def get_test_scores():
    counter = 0
    test_scores = []
    
    while True:
        test_score = int(input(f"Enter test score {counter +1} "
                               "(enter negative to stop): "))
        if test_score <  0 or test_score > 100:
            break
        test_scores.append(test_score)
        counter += 1
    return test_scores
        
        
def sort_scores(test_scores):
    test_scores.sort()
    test_scores.reverse()
    return test_scores


def display_result(test_scores):
    print(f"Sorted scores are: {test_scores}")
    
    
def main():
    test_scores = get_test_scores()
    sort_scores(test_scores)
    display_result(test_scores)
    
    
main()

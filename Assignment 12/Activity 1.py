# This program takes inputted test scores from 0-100 and outputs
# min, max and average 
#
# References:
# https://harpercollege.pressbooks.pub/programmingfundamentals
# /chapter/python-examples-6/


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
    return test_scores, counter
        
        
def calculate_min(test_scores):
    test_scores.sort()
    min = test_scores[0]
    return min


def calculate_max(test_scores, counter):
    max = test_scores[counter -1]
    return max
    
    
def calculate_average(test_scores, counter):
    total = sum(test_scores) 
    average = total / counter
    return average   
    

def display_result(min, max, average):
    print(f"Min: {min}, Max: {max}, Average: {average}")
    return
    
    
def main():
    test_scores, counter = get_test_scores()
    min = calculate_min(test_scores)
    max = calculate_max(test_scores, counter)
    average = calculate_average(test_scores, counter)    
    display_result(min, max, average)
    
    
main()

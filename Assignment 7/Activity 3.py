# This program takes input (miles) and asks which unit of measurement
# you would like to convert to and outputs the results.
#
# References:
# https://harpercollege.pressbooks.pub/programmingfundamentals/
# chapter/python-examples-4/
# https://www.mathsisfun.com/measure/us-standard-length.html

def get_distance():
    print("Enter distance in miles:")
    miles = float(input())
    return miles


def get_choice(): 
    print("Would you like to convert to
    Standard [S] or Metric [M]? [Enter S or M]")
    choice = input()
    return choice


def calculate_standard(miles):
    yards = miles * 1760
    feet = miles * 5280
    inches = feet * 12 
    miles_converted = f"{miles} miles is, {yards} yards long, {feet} 
    feet long, {inches} inches long." 
    return miles_converted


def calculate_metric(miles):
    kilometers = miles * 1.609344
    meters = kilometers * 1000
    centimeters = meters * 100
    miles_converted = f"{miles} miles is, {kilometers} KM long, {meters} 
    meters long, {centimeters} CM long."
    return miles_converted


def display_result(miles_converted):
    print(miles_converted) 


def main():
    miles = get_distance()
    choice = get_choice() 
    if choice == "S" or choice == "s":
        result = calculate_standard(miles)
        display_result (result)
    elif choice == "M" or choice == "m":
        result = calculate_metric(miles)
        display_result (result)
    else: 
        print("You must enter S or M to convert the distance")


main()

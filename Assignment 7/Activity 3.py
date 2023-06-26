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
    print("Would you like to convert to Standard [S]"
          " or Metric [M]? [Enter S or M]")
    choice = input()
    return choice


def calculate_yards(miles):
    yards = miles * 1760
    return yards


def calculate_feet(miles):
    feet = miles * 5280
    return feet


def calculate_inches(feet):
    inches = feet * 12
    return inches


def calculate_kilometers(miles):
    kilometers = miles * 1.609344
    return kilometers


def calculate_meters(kilometers):
    meters = kilometers * 1000
    return meters


def calculate_centimeters(meters):
    centimeters = meters * 100
    return centimeters


def display_sresult(miles, yards, feet, inches):
    print(
        f"{miles} miles is, {yards} yards,"
        f"{feet} feet and, {inches} inches long."
    )
    return 

def display_mresult(miles, kilometers, meters, centimeters):
    print(
        f"{miles} miles is, {kilometers} kilometers," 
        f"{meters} meters and, {centimeters} centimeters long."
    )
    return  

def main(): 
    miles = get_distance()
    choice = get_choice()
    if choice == "S" or choice == "s":
        yards = calculate_yards(miles)
        feet = calculate_feet(miles)
        inches = calculate_inches(feet)
        display_sresult(miles, yards, feet, inches)
    elif choice == "M" or choice == "m":
        kilometers = calculate_kilometers(miles)
        meters = calculate_meters(kilometers)
        centimeters = calculate_centimeters(meters)
        display_mresult(miles, kilometers, meters, centimeters)
    else: 
        print("You must enter S or M to convert the distance")


main()

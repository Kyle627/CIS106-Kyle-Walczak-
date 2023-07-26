# This program reads menu provided and outputs all items respectively.
# Then lists the total items, average calories, and average price.
#
# References:
# https://harpercollege.pressbooks.pub/programmingfundamentals
# /chapter/python-examples-8/
# https://youtu.be/K8L6KVGG-7o
# https://docs.python.org/3/library/stdtypes.html#str.isdigit
# https://stackoverflow.com/questions/22247957/
# regex-to-find-words-between-two-tags
# https://stackoverflow.com/questions/53574946/
# re-findall-return-separate-non-overlapping-results
# https://www.geeksforgeeks.org/sum-of-list-with-string-types-in-python/
# https://www.youtube.com/watch?v=ZUqGMDppEDs&t=613s&ab_channel=NeuralNine
import re


def read_menu(menu):
    try:
        with open(menu, "r") as file:
            for line in file:
                file = file.read()
                content = file.replace('$', '')
                return content
    except:
        print("File is missing")
        quit()


def get_item(content, tag):
    try:
        items = re.findall(f"<{tag}>(.*?)</{tag}>", content, re.DOTALL)
        return items
    except:
        print("File is empty")
        quit()

    
def display_result(names, price, calories, description):
    total_calories = sum([int(i) for i in calories if type(i) == int or
    i.isdigit()])
    average_calories = total_calories / len(calories)
    total_price = sum([float(i) for i in price if type(i) == str or
    i.isdigit()])
    average_price = total_price / len(price)
    counter = 0
    while counter < len(price):
        print(f"{names[counter]} - {description[counter]} - "
              f"{calories[counter]} - ${price[counter]} \n")
        counter += 1 
    print(f"{counter} Items - {average_calories:.0f} Average Calories - "
    f"${average_price:.2f} Average Price")


def main():
    menu = "simple.xml"
    content = read_menu(menu)
    names = get_item(content, "name")
    description = get_item(content, "description")
    calories = get_item(content, "calories")
    price = get_item(content, "price")
    display_result(names, price, calories, description)


main()

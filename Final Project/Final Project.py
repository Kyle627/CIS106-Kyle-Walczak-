# This program reads menu provided and outputs all items respectively.
# Then lists the total items, average calories, and average price.
#
# References:
# https://harpercollege.pressbooks.pub/programmingfundamentals
# /chapter/python-examples-8/
# https://youtu.be/K8L6KVGG-7o
# https://docs.python.org/3/library/stdtypes.html#str.isdigit
# https://stackoverflow.com/questions/22247957/regex-to-find-words-between-two-tags
import re

def read_menu(menu):
    try:
        with open(menu, "r") as file:
            for line in file:
                    content = file.read()
    except Exception:
        print("File not found")
    return content
    
def get_item(content):
    names = re.findall("<name>(.*?)</name>", content, re.DOTALL)
    description = re.findall("<description>(.*?)</description>", content, re.DOTALL)
    calories = re.findall("<calories>(.*?)</calories>", content, re.DOTALL)
    price = re.findall("<price>(.*?)</price>", content, re.DOTALL)
    return names, price, calories, description
    
    
def display_result(names, price, calories, description):
    i = 0
    while i < len(names):
        print(f"{names[i]} - {description[i]} - {calories[i]} - {price[i]} \n")
        i += 1 
    print(f"len({names} + 1) items")


def main():
    menu = "menu.xml"
    content = read_menu(menu)
    names = get_item(content)
    description = get_item(content)
    calories = get_item(content)
    price = get_item(content)
    display_result(names, price, calories, description)


main()

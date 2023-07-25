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
import re

def read_menu(menu):
    try:
        with open(menu, "r") as file:
            for line in file:
                    content = file.read()
    except Exception:
        print("File not found")
        return None
    return content


def get_item(content, tag):
    items = re.findall(f"<{tag}>(.*?)</{tag}>", content, re.DOTALL)
    return items 
    
    
def display_result(names, price, calories, description):
    i = 0
    while i < len(price):
        print(f"{names[i]} - {description[i]} - {calories[i]} - {price[i]} \n")
        i += 1 
    print(f" {i} items -")


def main():
    menu = "menu.xml"
    content = read_menu(menu)
    names = get_item(content, "name")
    description = get_item(content, "description")
    calories = get_item(content, "calories")
    price = get_item(content, "price")
    display_result(names, price, calories, description)


main()

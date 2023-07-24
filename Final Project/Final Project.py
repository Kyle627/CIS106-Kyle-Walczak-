# This program reads menu provided and outputs all items respectively.
# Then lists the total items, average calories, and average price.
#
# References:
# https://harpercollege.pressbooks.pub/programmingfundamentals
# /chapter/python-examples-8/
# https://youtu.be/K8L6KVGG-7o
import re

def read_menu(menu):
    try:
        with open(menu, "r") as file:
            for line in file:
                    content = file.read()
    except Exception:
        print("File not found")
    return content
    
    
def parse_content(content):
    cleaned_content = re.sub(r'<.*?>', '', content)
    return cleaned_content


def group_items(cleaned_content):
    name = []
    description = []
    calories = []
    price = [] 
    cleaned_content.strip()
    grouped = cleaned_content.split('\n')
    for item in grouped:
        if '$' in item:
            price.append(item)
        else:
            calroies = int(item)
            if calories > 0:
                calories.append(calories)
    print(f"{calories}")
    print(type(grouped))


def main():
    menu = "menu.xml"
    content = read_menu(menu)
    cleaned_content = parse_content(content)
    grouped = group_items(cleaned_content)
    
    
main()


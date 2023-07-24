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
    cleaned_content.strip()
    return cleaned_content


def group_items(cleaned_content):
    grouped = cleaned_content.split('\n')
    print(f"{grouped}")
    print(type(grouped))


def main():
    menu = "menu.xml"
    name = []
    description = []
    calories = []
    price = []
    content = read_menu(menu)
    cleaned_content = parse_content(content)
    grouped = group_items(cleaned_content)
    
    
main()


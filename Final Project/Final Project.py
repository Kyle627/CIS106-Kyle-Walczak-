# This program reads menu provided and outputs all items respectively.
# Then lists the total items, average calories, and average price.
#
# References:
# https://harpercollege.pressbooks.pub/programmingfundamentals
# /chapter/python-examples-8/
def read_menu(menu):
    try:
        with open(menu, "r") as file:
            for line in file:
                    content = file.read()
    except Exception:
        print("File not found")
    return content
    
    
def parse_content(content):
    print(f"{content}")


def main():
    menu = "menu.xml"
    content = read_menu(menu)
    parse_content(content) 
    
    
main()

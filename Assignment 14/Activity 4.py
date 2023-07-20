# This program takes file "add.txt" filled as
# an address book and outputs the address in 
# format: Lastname, Firstname, Address, City,
# State/Province/Region, PostalCode
#
# References:
# https://harpercollege.pressbooks.pub/programmingfundamentals
# /chapter/python-examples-7/
# https://harpercollege.pressbooks.pub/programmingfundamentals
# /chapter/python-examples-6/
# https://youtu.be/Uh2ebFW8OYM?t=378 

def read_file(file):
    try: 
        with open(file, "r") as file:
            file_content = file.read()
    except Exception as exception:
        print("ERROR: No file name found")
    return file_content


def sort_file(file_content):
    content = file_content.replace(",", "").replace("\n", " ")
    
    line1 = content[5:12] + ', ' + content[0:4] + ', ' + content[13:
    35] + ', ' + content[36:53] + ', ' + content[54:68]
    
    line2 = content[70:75] + ', ' + content[76:82] + ', ' + content[83:
    100] + ', ' + content[101:120] + ', ' + content[121:126]
    
    line3 = content[132:137] + ', ' + content[128:131] + ', ' + content[139:
    155] + ', ' + content[156:168] + ', ' + content[169:174]
    
    lines = [line1, line2, line3]
    return lines
    
    
def display_result(lines):
    print(f"{lines[0]}\n{lines[1]}\n{lines[2]}")
    return


def main():
    file = "add.txt"
    file_content = read_file(file)
    lines = sort_file(file_content)
    display_result(lines)
   
   
main()

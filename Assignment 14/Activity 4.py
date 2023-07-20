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
    except Exception:
        print("ERROR: No file name found")
        return
    return file_content


def sort_file(file_content):
    content = file_content.replace(",", "").replace("\n", " ")
    
    line1 = content[11:20] + ', ' + content[0:10] + ', ' + content[21:
    35] + ', ' + content[36:40] + ', ' + content[41:43] + ', ' + content[44:
    51] + '  '
    
    line2 = content[62:71] + ', ' + content[51:61] + ', ' + content[72:
    86] + ', ' + content[87:93] + ', ' + content[94:96] + ', ' + content[97:
    102]
    
    line3 = content[115:124] + ', ' + content[104:114] + ', ' + content[125:
    139] + ', ' + content[140:146] + ', ' + content[147:
    149] + ', ' + content[150:155]
    
    lines = [line1, line2, line3]
    return lines
    
    
def display_result(lines):
    print(f"{lines[0]}\n{lines[1]}\n{lines[2]}")
    return


def main():
    file = "addresses.txt"
    file_content = read_file(file)
    lines = sort_file(file_content)
    display_result(lines)
   
   
main()

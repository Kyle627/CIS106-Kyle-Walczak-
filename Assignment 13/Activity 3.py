# This program takes inputted variables (separated by commas)
# and output them on their own line without a comma or space.
#
# References:
# https://harpercollege.pressbooks.pub/
# programmingfundamentals/chapter/python-examples-7/
# https://harpercollege.pressbooks.pub/programmingfundamentals/
# chapter/string-functions/
# https://www.w3schools.com/python/ref_string_strip.asp


def get_variables():
    variables = []
    variables = input(f"Enter variables (separate each "
                          "variable with a comma): ")
    return variables


def split_variables(variables):
    variables = variables.split(',')
    return variables


def display_result(variables):
    for item in variables:
        print(item.strip())
    return
    
    
def main():
    variables = get_variables()
    variables = split_variables(variables)
    display_result(variables)


main()

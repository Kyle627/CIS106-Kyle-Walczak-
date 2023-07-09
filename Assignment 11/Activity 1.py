# This program take input from user on months and years
# and outputs the corresponding amount of days
#
# References:
# https://harpercollege.pressbooks.pub/
# programmingfundamentals/chapter/python-examples-6/
# https://www.w3schools.com/python/python_lists_access.asp

def get_year():
    print("What year would like to know about?")
    year = int(input())
    return year


def get_month():
    print("What month would you like to know about?")
    month = str(input())
    return month


def array_process(year, month):
    months = ['January', 'February', 'March', 'April',
              'May', 'June', 'July', 'September', 'October', 'November', 'December']
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if month  == 'February' and year % 4 == 0 and (year % 100 != 0
            or year % 400 == 0):
            days[1] = 29
    return days[months.index(month)]


def display_result(year, month, days):
    print(f" {month} {year} has {days} days")
    return 


def main():
    year = get_year()
    month = get_month()
    days = array_process(year, month)
    display_result(year, month, days)
    
    
main()

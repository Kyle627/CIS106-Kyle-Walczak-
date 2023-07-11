# This program take input from user on months and years
# and outputs the corresponding amount of days
#
# References:
# https://harpercollege.pressbooks.pub/
# programmingfundamentals/chapter/python-examples-6/
# https://www.w3schools.com/python/python_lists_access.asp
# https://www.w3schools.com/python/ref_list_insert.asp


months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
name_month = ['January', 'February', 'March', 'April',
              'May', 'June', 'July', 'August', 'September', 
              'October', 'November', 'December']
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def get_year():
    print("What year would like to know about?")
    year = int(input())
    return year


def get_month():
    print("What month would you like to know about?")
    month = int(input()) 
    if month < 1 or month > 12:
        print("Invalid month. Month must be between 0-12")
        quit()
    return month


def array_process(year, month):    
    if month == 2 and year % 4 == 0 and (year % 100 != 0 or 
        year % 400 == 0): 
        days.insert(1, 29)
    return days[months.index(month)]


def display_result(year, month, days):
    print(f"{name_month[month-1]} {year} has {days} days")
    return 


def main():
    year = get_year()
    month = get_month()
    days = array_process(year, month)
    display_result(year, month, days)
    
    
main()

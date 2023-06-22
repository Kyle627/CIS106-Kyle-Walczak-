# This program converts inputted age into months,
# days, hours, and seconds 
#
# References:
# https://harpercollege.pressbooks.pub/
# programmingfundamentals/chapter/python-examples-2/
# https://harpercollege.pressbooks.pub/
# programmingfundamentals/chapter/python-examples-3/
# https://www.scaler.com/topics/exit-in-python/

def get_age():
    print("Enter your age:") 
    years = int(input())
    return years


def cal_months(years):
    months = years * 12 
    return months


def cal_days(years):
    days = years * 365
    return days


def cal_hours(years):
    hours = years * 24
    return hours


def cal_seconds(hours):
    seconds = hours * 3600
    return seconds


def display_result(years, months, days, hours, seconds):
    print(" Being " + str(years) + " years old you are, " + str(months) +
    " months old, " + str(days) + " days old, " + str(hours) +
    " hours old, and " + str(seconds) + " seconds old. PHEW!") 


def main(): 
    years = get_age()
    months = cal_months(years)
    days = cal_days(years)
    hours = cal_hours(days)
    seconds = cal_seconds(hours)
    display_result(years, months, days, hours, seconds)


main()
exit()

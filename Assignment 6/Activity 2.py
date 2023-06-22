# This program converts inputted age into months,
# days, hours, minutes and seconds 
#
# References:
# https://harpercollege.pressbooks.pub/
# programmingfundamentals/chapter/python-examples-2/
# https://harpercollege.pressbooks.pub/
# programmingfundamentals/chapter/python-examples-3/

def get_age():
	print ("Enter your age:") 
	age_years = int(input())
	return age_years

def cal_months(age_years):
	months = age_years * 12 
	return months

def cal_days(age_years):
	days = age_years * 365.25
	return days

def cal_hours(days):
	hours = days * 24
	return days

def cal_seconds(days):
	seconds = days * 3600 
	return seconds

def display_result(age_years, months, days, hours, seconds):
	print(" Being " + str(age_years) + " years old you are, " + str(months) + " months old, " + str(days) + 
	" days old, " + str(hours) + " hours old, and " + str(seconds) + " seconds old. PHEW!") 

def main(): 
	age = get_age()
	months = cal_months(age)
	days = cal_days(age)
	hours = cal_hours(days)
	seconds = cal_seconds(hours)
	display_result(age, months, days, hours, seconds)

main()

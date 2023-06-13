# This program converts inputted age into months, days, 
# hours, minutes, and seconds.
#
# References:
# https://harpercollege.pressbooks.pub/programmingfundamentals/
# chapter/python-examples-1/
# https://harpercollege.pressbooks.pub/programmingfundamentals/
# chapter/python-examples-2/

print("What is your name?")
name_one = str(input())

print("What is your age in years? (X.25 = X and 3 months old, "
      ".50 = X and 6 months old, .75 = x and 9 months old)")
age_years = float(input()) 
age_months = int(age_years * 12)
age_days = int(age_years * 365.25)
age_hours = int(age_days * 24)
age_min = int(age_hours * 60)
age_sec = int(age_min * 60) 

print(str(name_one) + ", being " + str(age_years) + " years old you are: " + str(age_months) + " months old, " +
       str(age_days) + " days old, " + str(age_min) + " Minutes old, and " + str(age_sec) + " seconds old. PHEW!")

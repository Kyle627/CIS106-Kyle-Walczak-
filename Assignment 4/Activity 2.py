# This program converts inputted age into months, days, hours, minutes, and seconds.
#
# References:
# https://harpercollege.pressbooks.pub/programmingfundamentals/chapter/python-examples-1/
# https://harpercollege.pressbooks.pub/programmingfundamentals/chapter/python-examples-2/

print("What is your name?")
NameOne = str(input())

print("What is your age in years? (X.25 = X and 3 months old, .50 = X and 6 months old, .75 = x and 9 months old)")
AgeYears = float(input()) 
AgeMonths = int(AgeYears * 12)
AgeDays = int(AgeYears * 365.25)
AgeHours = int(AgeDays * 24)
AgeMin = int(AgeHours * 60)
AgeSec = int(AgeMin * 60 ) 

print(str(NameOne) + ", being " + str(AgeYears) + " years old you are: " + str(AgeMonths) + " months old, " + str(AgeDays) + " days old, " + str(AgeMin) + " Minutes old, and " + str(AgeSec) + " seconds old. PHEW!")



# This program displays your dogs age in puppy years when given human years
print("What is your Dog's name?")
dogsName = input()
print("How old is your dog, in human years?")
dogsAge = int(input())
dogHumanAge = dogsAge * 7
print(dogsName + " is " + str(dogHumanAge) + " years young, in human years! ")

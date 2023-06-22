def calRealAge(dogsAge):
    realAge = dogsAge * 7
    
    return realAge

def displayResult(dogsName, dogsAge, dogsRealAge):
    print(dogsName + " being " + str(dogsAge) + " is " + str(dogsRealAge) + " in human years.")

def getAge():
    print("What is your dogs age?")
    dogsAge = int(input())
    
    return dogsAge

def getName():
    print("What is your dogs name?")
    dogsName = input()
    
    return dogsName

# Main
# This program takes inputted dog age and name and outputs the converted age with a prompt.
dogsName = getName()
dogsAge = getAge()
dogsRealAge = calRealAge(dogsAge)
displayResult(dogsName, dogsAge, dogsRealAge)

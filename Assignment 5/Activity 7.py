def displayResult():
    print(dogsName + " being " + str(dogsAge) + " is " + str(dogsRealAge) + "in human years.")
    
    return 

def getAge():
    print("What is your dogs age?")
    dogsAge = int(input())
    
    return dogsAge

def getName():
    print("What is your dogs name?")
    dogsName = input()
    
    return dogsName

def getRealAge():
    realAge = dogsAge * 7
    
    return realAge

# Main
# This program takes inputted dog age and name and outputs the converted age with a prompt.
dogsName = getName()
dogsAge = getAge()
dogsRealAge = getRealAge()
displayResults()

firstNumber, secondNumber = 10, 20

def additionFunction ():
    newNumber = firstNumber + secondNumber
    return newNumber

def internalDeclaration ():
    firstNumber, secondNumber = 20, 20
    newNumber = firstNumber + secondNumber
    return newNumber

def externalDeclaration (firstNumber : int, secondNumber : int):
    newNumber = firstNumber + secondNumber
    return newNumber

if __name__ == '__main__':
    randomNumber = externalDeclaration (10, 10.0)
    print (randomNumber)
    # randomValue = additionFunction ()
    # print (f'Random Value : {randomValue}')


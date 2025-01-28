while True:
    try:
        n = 10
        inputNumber = int (input ('Enter the number\n'))
        result = n / inputNumber
        print (result)
        break
    except Exception:
        print ('There is some issue with your input')
    finally:
        print ('The execution of the code is completed')
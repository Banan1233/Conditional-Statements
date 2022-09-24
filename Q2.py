import ast


def input_type(inputr):
    try:
        return type(ast.literal_eval(inputr))
    except:
        return type(inputr)


def additionaloperations(number):
    print('\033[93m' + "\nAdditional Operations : " + '\033[0m')
    print('\033[93m' + "1. " + '\033[0m' + "Rounding number")
    print('\033[93m' + "2. " + '\033[0m' + "Number without a decimal point")
    print('\033[91m' + "3. " + "Exit" + '\033[0m')
    additionaloperation = input("Please Select Number Of Operation [1-3] : ")

    if len(additionaloperation) == 0:
        print('\033[91m' + "You should enter number of operation, Try Again" + '\033[0m')
        additionaloperation = input("Please Select Number Of Operation [1-3] : ")
    else:
        if not additionaloperation.strip().isdigit():
            print('\033[91m' + "Please enter numbers only, Try Again" + '\033[0m')
            additionaloperation = input("Please Select Number Of Operation [1-3] : ")
        else:
            if int(additionaloperation) > 3 or int(additionaloperation) <= 0:
                print('\033[91m' + "Please enter number from 1 to 6 only, Try Again" + '\033[0m')
                additionaloperation = input("Please Select Number Of Operation [1-3] : ")

    if int(additionaloperation) == 1:
        print('\033[93m' + "Round Options : " + '\033[0m')
        print('\033[93m' + "1. " + '\033[0m' + "Round to minimum number")
        print('\033[93m' + "2. " + '\033[0m' + "Round to number")
        print('\033[91m' + "3. " + "Exit" + '\033[0m')
        roundoption = input('\033[93m' + "Please Select Number Of Option [1-2] : " + '\033[0m')
        if len(roundoption) == 0:
            print('\033[91m' + "You should enter number of operation, Try Again" + '\033[0m')
            roundoption = input('\033[93m' + "Please Select Number Of Option [1-2] : " + '\033[0m')
        else:
            if not roundoption.strip().isdigit():
                print('\033[91m' + "Please enter numbers only, Try Again" + '\033[0m')
                roundoption = input('\033[93m' + "Please Select Number Of Option [1-2] : " + '\033[0m')
            else:
                if int(roundoption) > 2 or int(roundoption) <= 0:
                    print('\033[91m' + "Please enter number from 1 to 6 only, Try Again" + '\033[0m')
                    roundoption = input('\033[93m' + "Please Select Number Of Option [1-2] : " + '\033[0m')

        if int(roundoption) == 1:
            print('\033[92m' + "Final Result = " + '\033[0m' + f"{round(number)}")
        elif int(roundoption) == 2:
            roundnumber = input('\033[93m' + "Please Enter Number To Use in Rounding : " + '\033[0m')
            if len(roundnumber) == 0:
                print('\033[91m' + "You should enter number of operation, Try Again" + '\033[0m')
                roundnumber = input('\033[93m' + "Please Enter Number To Use in Rounding : " + '\033[0m')
            else:
                if not roundnumber.strip().isdigit():
                    print('\033[91m' + "Please enter numbers only, Try Again" + '\033[0m')
                    roundnumber = input('\033[93m' + "Please Enter Number To Use in Rounding : " + '\033[0m')
            print('\033[92m' + "Final Result = " + '\033[0m' + f"{round(number,int(roundnumber))}")
        elif int(roundoption) == 3:
            exit()
        else:
            print('\033[91m' + "Out of Range, Try Again" + '\033[0m')
            exit()
    elif int(additionaloperation) == 2:
        print('\033[92m' + "Final Result = " + '\033[0m' + f"{int(number)}")
    elif int(additionaloperation) == 3:
        exit()
    else:
        print('\033[91m' + "Out of Range, Try Again" + '\033[0m')
        exit()


print('\033[92m' + "Question 2" + '\033[0m')

number1 = input('\033[93m'+"Please Enter First Number : \n" + '\033[0m')
input_type(number1)
if len(str(number1)) == 0:
    print('\033[91m' + "You should enter first number, Try Again" + '\033[0m')
    exit()
else:
    if input_type(number1) is not float:
        if input_type(number1) is not int:
            print('\033[91m' + "Please enter numbers only, Try Again" + '\033[0m')
            exit()

number2 = input('\033[93m'+"Please Enter Second Number : \n" + '\033[0m')
if len(str(number2)) == 0:
    print('\033[91m' + "You should enter second number, Try Again" + '\033[0m')
    exit()
else:
    if input_type(number2) is not float:
        if input_type(number2) is not int:
            print('\033[91m' + "Please enter numbers only, Try Again" + '\033[0m')
            exit()

print('\033[93m'+"Operations : " + '\033[0m')
print('\033[93m'+"1. " + '\033[0m' + "+")
print('\033[93m'+"2. " + '\033[0m' + "-")
print('\033[93m'+"3. " + '\033[0m' + "*")
print('\033[93m'+"4. " + '\033[0m' + "/")
print('\033[93m'+"5. " + '\033[0m' + "^")
print('\033[93m'+"6. " + '\033[0m' + "%")
operation = input("Please Select Number Of Operation [1-6] [Digits] : ")
# print(operation)
if len(str(operation)) == 0:
    print('\033[91m' + "You should enter number of operation or digit of Operation, Try Again" + '\033[0m')
    operation = input("Please Select Number Of Operation [1-6] [Digits] : ")

if ((input_type(operation) is int) and (int(operation) == 1)) or operation == "+":
    operationEqual = float(number1) + float(number2)
    if (operationEqual - int(operationEqual)) == 0:
        operationEqual = int(operationEqual)
    print('\033[92m' + "Result = " + '\033[0m' + f"{operationEqual}")
    additionaloperations(operationEqual)
elif ((input_type(operation) is int) and (int(operation) == 2)) or operation == "-":
    operationEqual = float(number1) - float(number2)
    if (operationEqual - int(operationEqual)) == 0:
        operationEqual = int(operationEqual)
    print('\033[92m' + "Result = " + '\033[0m' + f"{operationEqual}")
    additionaloperations(operationEqual)
elif ((input_type(operation) is int) and (int(operation) == 3)) or operation == "*":
    operationEqual = float(number1) * float(number2)
    if (operationEqual - int(operationEqual)) == 0:
        operationEqual = int(operationEqual)
    print('\033[92m' + "Result = " + '\033[0m' + f"{operationEqual}")
    additionaloperations(operationEqual)
elif ((input_type(operation) is int) and (int(operation) == 4)) or operation == "/":
    operationEqual = float(number1) / float(number2)
    if (operationEqual - int(operationEqual)) == 0:
        operationEqual = int(operationEqual)
    print('\033[92m' + "Result = " + '\033[0m' + f"{operationEqual}")
    additionaloperations(operationEqual)
elif ((input_type(operation) is int) and (int(operation) == 5)) or operation == "^":
    operationEqual = int(number1) ^ int(number2)
    if (operationEqual - int(operationEqual)) == 0:
        operationEqual = int(operationEqual)
    print('\033[92m' + "Result = " + '\033[0m' + f"{operationEqual}")
    additionaloperations(operationEqual)
elif ((input_type(operation) is int) and (int(operation) == 6)) or operation == "%":
    operationEqual = float(number1) % float(number2)
    if (operationEqual - int(operationEqual)) == 0:
        operationEqual = int(operationEqual)
    print('\033[92m' + "Result = " + '\033[0m' + f"{operationEqual}")
    additionaloperations(operationEqual)
else:
    print('\033[91m' + "Please enter correct number of operation, Try Again" + '\033[0m')
    exit()

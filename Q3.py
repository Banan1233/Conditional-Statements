print('\033[92m' + "Question 3" + '\033[0m')
print('\033[93m' + "Enter 5 numbers to calc minimum & maximum number : " + '\033[0m')

Array = []
i = 0
maximum = 0
minimum = 0
try:
    while len(Array) < 5:
        print("Enter Number " + '\033[93m' + f"{i + 1}" + '\033[0m' + " : ")
        number = int(input())
        Array.append(number)
        if i == 0:
            minimum = number

        if number > maximum:
            maximum = number
        elif number < minimum:
            minimum = number
        i = i + 1
    print("Maximum Number is : " + '\033[93m' + f"{maximum}" + '\033[0m')
    print("Minimum Number is : " + '\033[93m' + f"{minimum}" + '\033[0m')
except:
    print('\033[91m' + "an error occurred, Try again" + '\033[0m')



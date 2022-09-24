print('\033[92m' + "Question 1" + '\033[0m')
name = input('\033[93m' + "Please Enter Your Name : \n" + '\033[0m')
if len(name) == 0:
    print('\033[91m' + "You should enter your Name, Try Again" + '\033[0m')
    exit()
else:
    if not name.replace(' ', '').isalpha():
        print('\033[91m'+"Your name is not Alphabet, Try Again"+'\033[0m')
        exit()

age = input('\033[93m' + "Please Enter Your Age : \n" + '\033[0m')
if len(age) == 0:
    print('\033[91m' + "You should enter your Age, Try Again" + '\033[0m')
    exit()
else:
    if not age.strip().isdigit():
        print('\033[91m'+"Your Age is not Number, Try Again"+'\033[0m')
        exit()

address = input('\033[93m' + "Please Enter Your Address : \n" + '\033[0m')
if len(address) == 0:
    print('\033[91m' + "You should enter your Address, Try Again" + '\033[0m')
    exit()
print("\n")
print(f"Hello Mr/Ms {name} age {age} located in {address}.\n thanks for beening one of our community,        Enjoy")

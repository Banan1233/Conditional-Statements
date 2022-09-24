Question = input('\033[92m' + "Please enter Question number : " + '\033[0m' + '\033[93m' + "[1-3]" + '\033[0m' + "\n")
if int(Question) == 1:
    print("=======================")
    import Q1
elif int(Question) == 2:
    print("=======================")
    import Q2
elif int(Question) == 3:
    print("=======================")
    import Q3

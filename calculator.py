def calculator():
    print(" ----> WELCOME TO CALCULATOR PYTHON PROGRAM <---- ")

    usr_inp_1 = int(input("\t Enter 1st Number: "))
    usr_inp_2 = int(input("\t Enter 2nd Number: "))

    Opretors = input("\n\t 1. +\n\t 2. -\n\t 3. *\n\t 4. %\n\t Enter your opretor:  ")

    if Opretors == '+':
        print(f"\n\t {usr_inp_1} + {usr_inp_2} = {usr_inp_1+usr_inp_2}")

    elif Opretors == '-':
        print(f"\n\t {usr_inp_1} - {usr_inp_2} = {usr_inp_1-usr_inp_2}")

    elif Opretors == '*':
        print(f"\n\t {usr_inp_1} * {usr_inp_2} = {usr_inp_1*usr_inp_2}")

    elif Opretors == '%':
        print(f"\n\t {usr_inp_1} % {usr_inp_2} = {usr_inp_1%usr_inp_2}")

    else :
        print("Enter correct  opretor")
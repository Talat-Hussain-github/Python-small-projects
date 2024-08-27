'''

This code includes the projects that I have done from scratch

'''
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit
from PyQt5.QtCore import Qt
import sys
import math
from datetime import datetime
import time






print("\n\t ---- WELLCOME TO THE PROJECTS OF PYTHON ---- ")

def Verification(): # First Step comes the verification where User should put password 

    password = 444

    while True:
        pass_user_1 = int(input("Enter Your password: "))
        if pass_user_1 == password:
            pass_user_2 = int(input("Enter Your password Again: "))

            if pass_user_2 == pass_user_1:
              print("\n\t Login success   ")
              after_login()
              
              
        else:
         print("Invalid password")

        

def after_login():
    Projects = int(input(f"\t MY PROJECTS (finished 1s) \n1. Calculator\n2. Age calculator\n3. To do list\n4. Ramdom Number game \n5. \n6. Save to file\n"))

    if Projects == 1:

        a = int(input("\n\t WHICH CALCULATOR \n 1. CLI (command line interface)\n 2. GUI (Grafhical user interface)\n"))
        if a == 1:
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

           calculator()
        elif a == 2:
            class Calculator(QMainWindow):
                def __init__(self):
                    super().__init__()
                    
                    self.setWindowTitle("Machine Esab")
                    
                    self.central_widget = QWidget()
                    self.setCentralWidget(self.central_widget)
                    
                    self.layout = QVBoxLayout()
                    self.central_widget.setLayout(self.layout)
                    
                    self.result_entry = QLineEdit()
                    self.result_entry.setAlignment(Qt.AlignRight)
                    self.result_entry.setReadOnly(True)
                    self.result_entry.setStyleSheet("font-size: 24px; padding: 10px;")
                    self.layout.addWidget(self.result_entry)
                    
                    self.button_grid = QGridLayout()
                    self.layout.addLayout(self.button_grid)
                    
                    buttons = [
                        ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
                        ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
                        ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
                        ('0', 3, 0), ('.', 3, 1), ('+', 3, 2), ('=', 3, 3),
                        ('sqrt', 4, 0), ('^', 4, 1), ('C', 4, 2), ('(', 4, 3),
                        (')', 5, 0), ('pi', 5, 1), ('e', 5, 2), ('exp', 5, 3)
                    ]

                    for text, row, col in buttons:
                        button = QPushButton(text)
                        button.setStyleSheet("font-size: 18px; padding: 15px;")
                        button.clicked.connect(lambda checked, t=text: self.on_button_click(t))
                        self.button_grid.addWidget(button, row, col)
                    
                    for i in range(6):
                        self.button_grid.setRowStretch(i, 1)
                    for i in range(4):
                        self.button_grid.setColumnStretch(i, 1)
                    
                    self.setGeometry(100, 100, 320, 480)  
                    self.current_input = ''

                def on_button_click(self, button_text):
                    if button_text == 'C':
                        self.current_input = ''
                    elif button_text == '=':
                        try:
                            expression = self.current_input.replace('^', '**').replace('sqrt', 'math.sqrt')
                            expression = expression.replace('pi', str(math.pi)).replace('e', str(math.e)).replace('exp', 'math.exp')
                            result = eval(expression)
                            self.current_input = str(result)
                        except Exception:
                            self.current_input = 'Error'
                    else:
                        self.current_input += button_text
                    self.result_entry.setText(self.current_input)

            app = QApplication(sys.argv)
            calculator = Calculator()
            calculator.show()
            sys.exit(app.exec_())
           
    elif Projects == 2:
        def age_calculator():
         print("\n\t---- WELCOME TO AGE CALCULATOR ----")

        year = int(input("\n\tEnter your birth year: "))
        month = int(input("\tEnter your birth month (1-12): "))
        day = int(input("\tEnter your birth day (1-31): "))

        from datetime import datetime

        birth_date = datetime(year, month, day)
        today = datetime.today()

        age = today - birth_date

        years = age.days // 365
        months = (age.days % 365) // 30
        days = (age.days % 365) % 30

        print(f"\n\tYou are {years} years, {months} months, and {days} days old.")

        age_calculator()









Verification()

'''
from datetime import datetime

print("\n\t ---- WELLCOME TO MY AGE CALCULATOR ---- ")

year = input("Enter the year: ")
month = input("Enter the month (1/12): ")
day = input("Enter the Day: ")

day_birth = datetime(year, month, day)
today = datetime.today()

age = day_birth - today

print(age)

years = age.days // 365
months = (age.days % 365) // 30
days = (age.days % 365) % 30

print(f"\n\tYou are {years} years, {months} months, and {days} days old.")


'''
# ------------------------------------------------------------------------



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
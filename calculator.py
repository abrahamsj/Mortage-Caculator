"""This program calculates the Monthly payments on a house- Mortage. it uses the following formula

M = P[r/n]/[1-[1+(r/n)]^ -nt],
where 
M = monthly payments
P = principle amount
r = interest rate for the term
n = # of months in a year
t = term (Length of loan in years)
""" 


import math # needed for the exponent part of the equation

# importing tkinter  for dialogue boxes
import easygui

def calculate_mortgage():
    try:
        P = float(easygui.enterbox("Enter your principal amount ($):"))
        t = int(easygui.enterbox("Enter the length of your loan in years:"))
        r = float(easygui.enterbox("Enter the interest rate for the term:"))

        n = 12  # assuming monthly payments
        M = (P * (r / n)) / (1 - (1 + (r / n)) ** (-n * t))

        easygui.msgbox(f"The mortgage on a house with a principal amount of ${P}, "
                       f"an interest rate of {r}, and a loan term of {t} years is ${M:.2f}")
    except ValueError:
        easygui.msgbox("Invalid input. Please enter valid numerical values.", "Error")

# Call the function to calculate mortgage
calculate_mortgage()







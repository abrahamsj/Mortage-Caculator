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
from tkinter import * 









n=12

print("Welcome!\n Lets calculate your Mortage")

P=int(input("Enter your principle amount:$"))
t=int(input("\nEnter the length of you loan in years, that is the term of your loan:"))
r=float(input("\nEnter the interest rate for the term:"))


M = (P*(r/n))/(1-(1+(r/n))**(-n*t)) 

print("The mortagage on a house with a principle amount of $",P,",an interest rate of ",r,"and a loan term of",t," is ",M)



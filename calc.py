
from cmath import sqrt
from math import pow 

sum = 1
subtraction = 2
division = 3
multiplication = 4
division = 5
percentage = 6

print("Operators avaible, please write one in the correct order : sum, subtraction, multiplication, division, percentage, power, sqaureroot")
op = input()
if op == "sum":
    print("Choose a specific value for the first number to count the sum")
    a = float(input())
    print("Choose a specific value for the second number to count the sum")
    b = float(input())
    print("The result of this operation is", a+b)
elif op == "subtraction":
    print("Choose a specific value for the first number to count the subtraction")
    a = float(input())
    print("Choose a specific value for the second number to count the subtraction")
    b = float(input())
    print("The result of this operation is", a-b)
elif op == "multiplication":
    print("Choose a specific value for the first number to count the multiplication")
    a = float(input())
    print("Choose a specific value for the second number to count the multiplication")
    b = float(input())
    print("The result of this operation is", a*b)
elif op == "division":
    print("Choose a specific value for the first number to count the division")
    a = float(input())
    print("Choose a specific value for the second number to count the division")
    b = float(input())
    print("The result of this operation is", a/b)
elif op == "percentage":
    print("Choose a specific value for the first number to count the percentage")
    a = float(input())
    print("Choose a specific value for the second number to count the percentage")
    b = float(input())
    print("The result of this operation", a%b)
elif op == "sqaureroot":
    print("Choose a specific value to count it's sqaureroot")
    a = float(input())
    print("The sqaureroot of a is", sqrt(a))
elif op == "power":
    print("Choose a number to count it's power ")
    c=float(input())
    print("Choose a power")
    d=float(input())
    print("The result of this power operation is", pow(c, d))
else:
    print("You've entered an invalid expression, please try writing the operation in the right order.")

from cmath import sqrt

sum = 1
subtraction = 2
division = 3
multiplication = 4
division = 5
percentage = 6

print("Choose a specific value for the first number")
a = float(input())
print("Choose a specific value for the second number")
b = float(input())
print("Write an operator : sum, subtraction, multiplication, division, percentage, sqaure, sqaureroot")
op = input()
if op == "sum":
    print("The result of this operation is", a+b)
elif op == "subtraction":
    print("The result of this operation is", a-b)
elif op == "multiplication":
    print("The result of this operation is", a*b)
elif op == "division":
    print("The result of this operation is", a/b)
elif op == "percentage":
    print("The result of this operation", a%b)
elif op == "sqaure":
    print("The sqaure of a is", a*a, "the sqaure of b is", b*b)
elif op == "sqaureroot":
    print("The sqaureroot of a is", sqrt(a), "The sqaureroot of b is", sqrt(b))
else:
    print("You've entered an invalid operator, or you didnt write it in the correct order")

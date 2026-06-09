#VihaanPhapale(June 8th)
#Int: 10, Float: 6.4, String: "hi", Boolean: True
#
# fl = 10.6
# num = int(fl)
# print(num)
#
# num = 10
# fl = float(num)
# print(fl)
#
# st = "15"
# num = int(st)
# print(num)
#
# +, -, *, /, %, **, //
# 1+1 = 2
# 1-1 = 0
# 3*4 = 12
# 12/5 = 2.4
# 12 % 7 = 5
# 2**3 = 8
# 15//8 = 1
#
# print("dog " + "cat")
# print("dog" * 2)
#
# <, >, <=, >=, ==, !=
#
# or, and, not, not in, in
#
import operator

ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

# Get first number safely
num1 = input("Enter first number: ")
while not num1.isdigit():
    num1 = input("Please enter a valid integer: ")
num1 = int(num1)

# Get operator safely
op = input("Enter operator (+, -, *, /): ")
while op not in ops:
    op = input("Enter a valid operator (+, -, *, /): ")

# Get second number safely
num2 = input("Enter second number: ")
while not num2.isdigit():
    num2 = input("Please enter a valid integer: ")
num2 = int(num2)

# Compute result
result = ops[op](num1, num2)

print("Result:", result)
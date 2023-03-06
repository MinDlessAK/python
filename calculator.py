#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      akash
#
# Created:     15-01-2022
# Copyright:   (c) akash 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
#Our Calculator

first = input("Enter first number : ")
second = input("Enter second number : ")
first = int(first)
second = int(second)
print("----press keys for operator (+,-,*,/,%)----------")
operator = input("Enter operator : ")

if operator == "+":
   print(first + second)
elif operator == "-":
   print(first - second)
elif operator == "*":
   print(first * second)
elif operator == "/":
   print(first / second)
elif operator == "%":
   print(first % second)
else:
   print("Invalid Operation")

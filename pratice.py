#-------------------------------------------------------------------------------
# Name:        module1
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
first=input("enter your number:")
second=input("enter your number:")
first=int(first)
second=int(second)
print("-------the operator are(+,-,*,/,%)")
operator=input("enter operator:")
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

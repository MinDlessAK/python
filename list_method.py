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
marks = ["english", 95, "chemistry", 98]
marks.append("physics")
marks.append(97)
print(marks)

marks.insert(0, "math")
marks.insert(1, 99)
print(marks)

print("math" in marks)

print(len(marks)/2)
marks.clear()
print(marks)




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
students = ["ram", "shyam", "kishan", "radha", "radhika"]

for student in students:
   if(student == "radha"):
       break
   print(student)

for student in students:
   if(student == "kishan"):
       continue
   print(student)

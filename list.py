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
friends = ["amar", "akbar", "anthony"]
print(friends[0])
print(friends[1])
print(friends[-1])
print(friends[-2])

friends[0] = "aman"
print(friends)

print(friends[0:2]) #returns a new list

for friend in friends:
   print(friend)


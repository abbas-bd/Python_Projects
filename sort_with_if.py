#!/bin/python3
#
#This program takes 3 input numbers from the user and displays them as smaller to larger numbers in the output.and can also recognize equal numbers.
#NOTE:This program is written using condition only. To better understand the "IF" command in Python
print ()
print ("enter '3' input number:")
num1 = int(input("input 1: "))
num2 = int(input("input 2: "))
num3 = int(input("input 3: "))
print ()
##
if num1 < num2 < num3 :
     print (num1,num2,num3)
elif num2 < num1 < num3 :
    print (num2 , num1 , num3)
elif num3 < num2 < num1 :
    print (num3 , num2 , num1)
elif num2 < num1 < num3 :
    print (num2 , num1 , num3)
elif num1 < num3 < num2 :
    print (num1 , num3 , num2)
elif num3 < num1 < num2 :
    print (num3 , num1 , num2)
## "=="
elif num1 == num2 == num3 :
    print ("ERR: all input numbers equal")
elif num1 == num2 > num3 :
    print (num3,num1,num2)
elif num1 < num2 == num3 :
    print (num1,num2,num3)
elif num2 < num1 == num3 :
    print (num2,num1,num3)

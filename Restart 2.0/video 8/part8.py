# To check the given number is armstrong or not
from math import *
def length(num:int)->int:
    return int(log10(num) + 1)

def armstrong(num:int):
    l = length(num)
    arm_number = 0
    n = num
    while n > 0:
        rem = n % 10
        arm_number = arm_number + rem ** l 
        n = n // 10
    return arm_number


num = int(input("Enter any number: "))
if num == armstrong(num):
    print("The given number is armstrong.")
else:
    print("The given number is not armstrong.")

# Count no of digits in number
from math import *
def length(num:int)->int:
    return int(log10(num) + 1)

num = int(input("Enter any number: "))
print(f"The length of {num} is {length(num)}")

'''Time complexity for this method is o(1).'''
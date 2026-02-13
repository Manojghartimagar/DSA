from math import *
num = int(input("Enter any number: "))
count = int(1 + log10(num))
print(f"no of digit in {num} is {count}.")

# count = 0
# while num>0:
#     count+=1
#     num = int(num/10)

# print(count)

# time complecity is o(log10 ),log5,log2.space complecity is o(1)
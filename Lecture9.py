# num = int(input("Enter number: "))
# result = []
# count = 0
# for i in range(1,num +1):
#     if(num % i == 0):
#         result.append(i)

# print(result)

#TC = O(n)  SC = O(k)


# better solution

# result = []
# num = int(input("Enter any number: "))
# for i in range(1,int(num/2) + 1):
#     if(num % i ==0):
#         result.append(i)
# result.append(num)
# print(result)
# #TC = O(n/2) almost=to O(n)  SC = O(k)

# optimal solution

from math import sqrt
result = []
num = int(input("Enter any number: "))
for i in range(1,int(sqrt(num)) + 1):
    if(num % i == 0):
        result.append(i)
        if(num/i != i):
            result.append(int(num/i))
result.sort()
print(result)


# TC = O(sqrt(n)) + O(NlogN) SC = O(k)
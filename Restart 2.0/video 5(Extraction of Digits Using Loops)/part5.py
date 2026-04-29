'''Uses Extraction of Digits from number to'''
def Extraction(num:int):
    n = num
    while n > 0:
        rem = n % 10
        print(rem)
        n = n//10

num = int(input("Enter any number: "))
Extraction(num)
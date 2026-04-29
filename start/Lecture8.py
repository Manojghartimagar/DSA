# from math import log10

num = int(input("Enter any number: "))

if num == 0:
    print(True)
else:
    num1 = num
    result = 0
    n = len(str(num))
    # n = int(1 + log10(num))

    while num > 0:
        r = num % 10
        result += r ** n
        num //= 10

    print(num1 == result)

#TC  = O(log10(n)) SC = O(1)
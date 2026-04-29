num = int(input("Enter any number: "))
num1 = num
newnum = 0
while num > 0:
    r = num % 10
    newnum = newnum*10 + r
    num = int(num /10)

print(num1 == newnum)

#sc = O(1) TC = O(log10(n))
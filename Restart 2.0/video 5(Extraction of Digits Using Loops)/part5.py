# Count no of digits in number
def length(num:int)->int:
    count = 0
    n = num
    while n > 0:
        count += 1
        rem = n % 10
        n = n//10
    return count

num = int(input("Enter any number: "))
print(f"The length of {num} is {length(num)}")
# Factorial of numbers
def fact(num:int)->int:
    if num == 1 or num == 0:
        return 1
    return fact(num - 1 ) * num

num = int(input("Enter nay number: "))
print(f"The factorial of {num} is {fact(num)}")
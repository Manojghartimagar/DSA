# Functional Recursion
def sum(num:int)->int:
    if num == 1:
        return 1
    return sum(num-1) + num

num = int(input("Enter any number: "))
print(f"The sum of {num} is {sum(num)}")
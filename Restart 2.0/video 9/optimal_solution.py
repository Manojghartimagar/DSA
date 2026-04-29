#Print all factors of a given numbers(optimal solution)
from math import sqrt
def factors(num: int) -> list:
    result = []
    for i in range(1, int(sqrt(num)) + 1):
        if num % i == 0:
            if i == num // i:
                result.append(i)
            else:
                result.append(i)
                result.append(num // i)
    
    result.sort()   # sort separately
    return result

num = int(input("Enter a number: "))
print(f"The factors of {num} are {factors(num)}")

# The time complexity for this method is o(sqrt(N)) + o(Nlog(N)) and space complexity is o(k)
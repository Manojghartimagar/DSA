#Print all factors of a given numbers
def factors(num:int)->list:
    result = []
    for i in range(1,num + 1):
        if num % i == 0:
            result.append(i)
    return result

num = int(input("Enter a number: "))
print(f"The factors of {num} is {factors(num)}")

# The time complexity for this method is o(N) and space complexity is o(k)
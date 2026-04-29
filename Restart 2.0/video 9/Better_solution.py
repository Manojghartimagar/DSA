#Print all factors of a given numbers(Better solution)
def factors(num:int)->list:
    result = []
    for i in range(1,num // 2):
        if num % i == 0:
            result.append(i)
    result.append(num)
    return result

num = int(input("Enter a number: "))
print(f"The factors of {num} is {factors(num)}")

# The time complexity for this method is o(N/2) == o(N) and space complexity is o(k)
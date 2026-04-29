# To calculate reverse number and check the palindrome
def reverse(num:int)->int:
    n = num
    rev_num = 0
    while n > 0:
        rem = n % 10
        rev_num = rev_num * 10 + rem 
        n = n//10
    return rev_num

num = int(input("Enter any number: "))
if num == reverse(num):
    print("The number is palindrome.")
else:
    print("The number is not palindrome.")

# Time complexity for this progrme is o(log(N)) and Space complexity is o(1)
# Check if a string is palindrome or not By Loop
string = input("Enter a string: ")
i = 0
j = len(string) -1
value = True
while i <= len(string)//2:
    if string[i] != string[j]:
        value = False
        break
    i += 1
    j -= 1
if value == True:
    print("The given string is palindrome.")
else:
    print("The given string is not palindrome.")
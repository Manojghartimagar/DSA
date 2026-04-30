def Is_palindrome(l,r,string):
    if l >= r:
        return True
    if string[l] == string[r]:
        return Is_palindrome(l+1,r-1,string)
    else:
        return False

string = input("Enter a string: ")
if Is_palindrome(0,len(string)-1,string) == True:
    print("The given string is palindrome.")
else:
    print("The given string not palindrome.")
    
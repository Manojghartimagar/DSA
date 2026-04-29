# def func(s,l,r):
#     while l<r:
#         if s[l] != s[r]:
#             return False
#         l+=1
#         r-=1
#     return True
    
# string = input("Enter any string: ")
# if func(string,0,len(string)-1) == True:
#     print(f"The string {string} is palindrome.")





def func(str: str,l,r):
    if l>=r:
        return
    elif str[l] != str[r]:
        return False
    else:
        func(str,l+1,r-1)
        return True
    

string = input("Enter any string: ")
if func(string,0,len(string)-1) == True:
    print("The string is palindrome.")
else:
    print("The string is not palindrome.")

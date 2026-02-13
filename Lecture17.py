def func(s,l,r):
    while l<r:
        if s[l] != s[r]:
            return False
        l+=1
        r-=1
    return True
    
string = input("Enter any string: ")
if func(string,0,len(string)-1) == True:
    print(f"The string {string} is palindrome.")
    

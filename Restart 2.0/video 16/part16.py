# Reverse an Array Using Recursion
num = [5,7,3,2,6,1,5,9]
def reverse(l,r,num):
    if l >= r:
        return num
    num[l],num[r] = num[r],num[l]
    return reverse(l+1,r-1,num)

print(reverse(2,5,num))
print(reverse(0,7,num))

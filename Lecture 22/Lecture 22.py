from Lecture22 import merge

def Merse_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2

    left_arr = arr[:mid]
    right_arr = arr[mid:]

    left = Merse_sort(left_arr)
    right = Merse_sort(right_arr)

    return merge(left,right)

print(Merse_sort([1,3,4,8,2,0,5,8,9,10,7,3,6]))

#Tc = o(log2(n))
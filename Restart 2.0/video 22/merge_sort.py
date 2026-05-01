# Merge Sort
from merge_function import merge
def merge_sort(arr):
    if len(arr) == 1:
        return arr
    left_arr = arr[ : len(arr) // 2]
    right_arr = arr[len(arr) // 2 : ]
    left = merge_sort(left_arr)
    right = merge_sort(right_arr)
    return merge(left,right)

arr = [3,1,2,4,1,5,2,6,4]
print(merge_sort(arr))

# Time complexity = o(NlogN) and sc = o(N)
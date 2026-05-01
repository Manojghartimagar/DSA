# Quick Sort
from Pivot import partition
def quick_sort(nums,low,high):
    if low < high:
        p_index = partition(nums,low,high)
        quick_sort(nums,low,p_index-1)
        quick_sort(nums,p_index + 1,high)
    return nums

print(quick_sort([4,1,7,6,3,2,8],0,6))

# time complexity = o(nlogn) in best case and o(n*n) in worst case sc = o(1)

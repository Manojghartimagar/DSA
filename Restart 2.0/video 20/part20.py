# Bubble Sort
def bubble_sort(nums):
    for i in range(len(nums)-1,-1,-1):

        for j in range(i):
            if nums[j] >= nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
    return nums
print(bubble_sort([5,8,1,6,9,2,4]))

# time complexity = o(N(N+1)/2)==o(n**2)
def bubble_sort(nums):
    n = len(nums)
    for i in range(n-1,-1,-1):
        for j in range(i):
            if nums[j] >= nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
    return nums
print(bubble_sort([5,8,1,6,9,2,4]))
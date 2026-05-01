def bubble_sort(nums):
    n = len(nums)
    for i in range(n-1,-1,-1):
        is_swape  = False
        for j in range(i):
            if nums[j] >= nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
                is_swape = True
        if is_swape == False:
            print("Best case!")
            return nums
    return nums
print(bubble_sort([1,2,3,4,5,6,7,8]))

# time complexity = o(n)
# nums = [5, 7, 8, 4, 1, 6, 9, 2]

# n = len(nums)
# for i in range(n):
    
#     for j in range(0, n - i - 1):
#         if nums[j] > nums[j + 1]:
#             nums[j], nums[j + 1] = nums[j + 1], nums[j]

# print(nums)

# def bubble_sort(nums):
#     for i in range(len(nums)):
#         for j in range(len(nums)-i-1):
#             if nums[j] <= nums[j+1]:
#                 nums[j], nums[j + 1] = nums[j + 1], nums[j]
#     return nums

# print(bubble_sort([5, 7, 8, 4, 1, 6, 9, 2]))

# TC = O(N(N+1)/2) SC = O(1)

def bubble_sort(nums):
    for i in range(len(nums)):
        is_swape = False
        for j in range(len(nums)-i-1):
            if nums[j] >= nums[j+1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                is_swape = True
        if is_swape == False:
            print("O(N)")
            return nums
        
print(bubble_sort([1,2,3,4,5,6,7,8,9,10]))


# TC = O(N) SC = O(1)

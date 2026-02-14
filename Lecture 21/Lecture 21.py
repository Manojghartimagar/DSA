# nums = [3,5,6,4,8,9,10,7,1]

# for i in range(1,len(nums)):
#     key = nums[i]
#     j = i-1
#     while j >= 0 and nums[j] >= key:
#         nums[j+1] = nums[j]
#         j-=1
#     nums[j+1] = key

# print(nums)

def insertion_sort(nums):
    for i in range(1,len(nums)):
        key = nums[i]
        j = i-1

        while j >= 0 and nums[j] <= key:
            nums[j+1] = nums[j]
            j = j-1
        
        nums[j+1] = key
    print(nums)
    return 

insertion_sort([1,56,39,50,20,46,82,91,99,36,57])

# TC = O(N(N+1)/2) SC = O(1)


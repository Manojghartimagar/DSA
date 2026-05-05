def linear_search(nums,target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1
        
print(linear_search([5,3,9,8,1,6,4,-1,-100],4))

# Time complexity = o(N) sc = o(1)
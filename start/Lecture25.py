nums = [55,32,-97,99,3,88,67]
# nums.sort()
# print(nums[(len(nums)-2)])

# TC = O(nlogn) SC = O(1)

largest = float("-inf")
s_largest  = float("-inf")
for i in range(len(nums)):
    largest = max(largest,nums[i])

    
for i in range(len(nums)):
    if s_largest <= nums[i] and nums[i] < largest:
        s_largest = nums[i]
print(nums)
print(largest)
print(s_largest)
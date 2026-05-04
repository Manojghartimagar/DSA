# Remove Duplicates From a Sorted Array(In place)
nums = [1,1,1,2,3,4,5,5,6,6,6,6,6,7,7,8,8,8,9,9,9,9,10,10]
n = len(nums)
nums_dict = {}
for i in range(n):
    nums_dict[nums[i]] = 0

j = 0
for i in nums_dict:
    nums[j] = i
    j+=1
print(nums)

# Time complexity = o(N) and Space complexity = o(N)
# By using slicing
def reverse(nums:list,k:int):
    n = len(nums)
    nums[:] = nums[n-k:] + nums[:n-k]

nums = [1,2,3,4,5,6,7,8,9]
reverse(nums,5)
print(nums)

# TC = o(N) sc = o(1)

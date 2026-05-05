# My idea to solve question
def move_zeros_to_end(nums):
    n = len(nums)
    i,j = 0,1
    while j < n:
        if nums[j] != 0:
            i += 1
            nums[i],nums[j] = nums[j],nums[i]
        j += 1

nums = [1,0,2,4,3,0,0,3,5,1]
move_zeros_to_end(nums)
print(nums)

# time complexity = o(N) ans space complexity = o(1)

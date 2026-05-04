# Right rotate an array by one place
nums = [5,-2,3,9,0,6,10,7]
tem = nums[len(nums)-1]
for i in range(len(nums)-2,-1,-1):
    nums[i+1] = nums[i]
nums[0] = tem
print(nums)
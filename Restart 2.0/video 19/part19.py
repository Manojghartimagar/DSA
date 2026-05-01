# Selectiion Sort
nums = [5,8,7,4,6,9,2]
for i in range(len(nums)):
    min_index = i
    for j in range(i+1,len(nums)):
        if nums[min_index] >= nums[j]:
            min_index = j
    nums[i],nums[min_index] = nums[min_index],nums[i]

print(nums)
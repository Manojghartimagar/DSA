nums = [55,32,-97,99,99,-97,3,67]
print(nums)
largest = nums[0]
mini  = nums[0]

for i in range(1,len(nums)):
    largest = max(largest,nums[i])
    mini = min(mini,nums[i])

print(largest)
print(mini)

#TC = O(n) SC = O(1)


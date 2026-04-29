# nums = [1,1,1,2,2,3,3,4,4,5,5,6,6,6,6,6,6,7,7,7,8,8,8,9]
# k = 1
# for i in range(1, len(nums)):
#     if nums[i] != nums[i-1]:
#         nums[k] = nums[i]
#         k += 1

# print(nums[:k])

nums = [1,1,1,2,2,3,3,4,4,5,5,6,6,6,6,6,6,7,7,7,8,8,8,9]

hash_dics = {}

for num in nums:
    if num not in hash_dics:
        hash_dics[num] = 1

k = 0
for key in hash_dics:
    nums[k] = key
    k += 1

print(hash_dics)
print(nums[:k])

# Frequestion map and Dictionary
# this is {1:2,2:1,3:4,4:2,5:3} from nums = [1,2,3,1,4,3,5,4,5,5,3,3]
"""method 1"""
nums = [1,2,3,1,4,3,5,4,5,5,3,3]
freq_map = {}
for i in range(len(nums)):
    if nums[i] in freq_map.keys():
        freq_map[nums[i]] += 1
    else:
        freq_map[nums[i]] = 1

print(freq_map)

"""method 2"""
hash_map = {}
for i in nums:
    hash_map[i] = hash_map.get(i,0) + 1

print(hash_map)

# Time complexity = o(n) and space complexity = o(n)
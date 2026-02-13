# Method1
nums = [5,6,7,7,1,9,111,1,1,5,1,1]
dics = {}
# for i in nums:
#     if i in dics.keys():
#         dics.update({i:dics[i]+1})
#     else:
#         dics.setdefault(i,1)

for i in range(0,len(nums)):
    dics[nums[i]] = dics.get(nums[i],0) + 1

print(dics)

# TC  = O(N) SC = O(N)
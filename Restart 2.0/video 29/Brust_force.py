# brust force solution to right rotate array by kth time
def reverse(nums:list,k):
    n = len(nums)
    rorate = k % n
    for i in range(k):
        e = nums.pop() # TC = o(1)
        nums.insert(0,e) # TC = o(N)
nums = [1,2,3,4,5,6,7,8,9]
reverse(nums,5)
print(nums)

# TC = o(N*K) sc = o(1)


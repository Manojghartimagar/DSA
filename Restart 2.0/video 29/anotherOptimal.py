# By using reverse formula

def reverse(nums,l,r):
    if l<r:
        nums[l],nums[r] = nums[r],nums[l]
        reverse(nums,l+1,r-1)


nums = [1,2,3,4,5,6,7,8,9]
k,n = 5,len(nums)

reverse(nums,n-k,n-1)  # TC = o(K/2)
reverse(nums,0,n-k-1)  # TC = o((N-K)/2)
reverse(nums,0,n-1)  # TC = o(N/2)

print(nums)

# the final time complexity = o(N) sc = o(1)
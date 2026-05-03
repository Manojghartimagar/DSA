# To find largest number in array
def largest_number(nums):
    largest = float("-inf")
    for i in range(1,len(nums)):
        largest = max(largest,nums[i])
    return largest
print(largest_number(nums = [55,32,-97,99,3,67]))

# Time complexity = o(N) and space complexity = o(1)
# To find second largest number in array (Better solution)
def second_largest_number(nums):
    largest = nums[0]
    for i in range(1,len(nums)):
        largest = max(largest,nums[i])
    
    sec_large = float("-inf")
    for j in range (1,len(nums)):
        if nums[j] != largest:
            sec_large = max(sec_large,nums[j])   
    return sec_large
print(second_largest_number(nums = [55,32,-97,99,3,67]))

# Time complexity = o(N) and space complexity = o(1)


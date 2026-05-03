# To find second largest number in array (optimal solution)
def second_largest_number(nums):
    sec_large = float("-inf")
    largest = float("-inf")
    for i in range(len(nums)):
        if nums[i] > largest:
            sec_large = largest
            largest = nums[i]
        else:
            sec_large = max(sec_large,nums[i])   
            
    return sec_large
print(second_largest_number(nums = [55,32,-97,99,3,67]))

# Time complexity = o(N) and space complexity = o(1)
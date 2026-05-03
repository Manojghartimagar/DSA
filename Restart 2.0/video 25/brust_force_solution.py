# To find second largest number in array (brust force solution)
def second_largest_number(nums:list)->int: 
    nums.sort()
    second_largest = nums[-2]
    return second_largest

print(second_largest_number(nums = [55,32,-97,99,3,67]))
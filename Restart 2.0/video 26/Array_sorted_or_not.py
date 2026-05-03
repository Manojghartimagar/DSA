# Check if Array is sorted or not
def sorted(nums:list)->bool:
    for i in range(len(nums)-1):
        if nums[i+1] < nums[i]:
            return False
        return True
if sorted(nums = [3,5,6,8,9,10,20]) == True:
    print("The array is sorted.")
else:
    print("The array is not sorted.")

# time complexity = o(N) sc = o(1)
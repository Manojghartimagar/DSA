#I use Bubble sort

def bubble_sort(nums):
    is_sort = False
    for j in range(len(nums)-1):
        if nums[j] >= nums[j+1]:
            is_sort = True

    if is_sort == False:
        return True
    
    return False
    
if bubble_sort([1,2,3,4,5,6,9,7,8]) and True:
    print("The list is sorted.")
else:
    print("List is not sorted.")
#git pull origin main --rebase
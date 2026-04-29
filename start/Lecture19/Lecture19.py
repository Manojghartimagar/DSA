# nums = [5,7,8,4,1,6,9,2]

# for i in range(0,len(nums)):
#     min_index = i
#     for j in range(i+1,len(nums)):
#         if nums[min_index]>=nums[j]:
#             min_index = j
#     nums[i],nums[min_index] = nums[min_index],nums[i]

# print(nums)


def selection_sort(nums:list)->list:
    for i in range(0,len(nums)):
        max_index = i
        for j in range(i+1,len(nums)):
            if nums[j] >= nums[max_index]:
                max_index = j
        nums[i],nums[max_index] = nums[max_index],nums[i]
    return nums




nums = [5,7,8,4,1,6,9,2]
print(selection_sort(nums))



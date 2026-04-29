def partition(nums,l,h):
    pivot = nums[l]
    i,j = l,h

    while i<j:
        while nums[i] <= pivot and i <= h - 1:
            i+=1

        while nums[j] >= pivot and j >=l+1:
            j-=1
        
        if i<j :
            nums[i],nums[j] = nums[j],nums[i]
    
    nums[l],nums[j] = nums[j],nums[l]
    return j


def Merge(left,right):
    merge_sort = []
    l,r = len(left),len(right)
    i,j = 0,0
    while i<l and j<r:
        if left[i] == right[j]:
            merge_sort.append(left[i])
            i+=1
            j+=1
        else:
            if left[i] in merge_sort and right[j] in merge_sort:
                i+=1
                j+=1
            elif left[i] in merge_sort and right[j] not in merge_sort:
                merge_sort.append(right[j])
                i+=1
                j+=1
            elif left[i] not in merge_sort and right[j] not in merge_sort:
                if left[i]<right[j]:
                    merge_sort.append(left[i])
                    i+=1
                else:
                    merge_sort.append(right[j])
                    j+=1
            else:
                merge_sort.append(left[i])
                i+=1
                j+=1
    
    if i<l:
        while i<l:
            merge_sort.append(left[i])
            i+=1
    
    if j<r:
        while j<r:
            merge_sort.append(right[j])
            j+=1
    return merge_sort

print(Merge([1,1,1,2,4,6,7],[1,2,3,3,6,7,8,9,10]))

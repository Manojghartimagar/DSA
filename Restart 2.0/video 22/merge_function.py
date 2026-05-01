def merge(left,right):
    m = len(left)
    n = len(right)
    merge = []
    i = 0
    j =0
    while i < m and j < n:
        if left[i] <= right[j]:
            merge.append(left[i])
            i += 1
        else:
            merge.append(right[j])
            j += 1
    
    if i < m:
        for x in range(i,m):
            merge.append(left[x])
        
    else:
        for x in range(j,n):
            merge.append(right[x])
    return merge
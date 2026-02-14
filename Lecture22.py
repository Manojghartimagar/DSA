def merge(left,right):
    result = []
    i,j = 0,0
    m,n = len(left),len(right)
    while i<m and j<n:
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    
    if i < m:
        while i<m:
            result.append(left[i])
            i+=1
        
    if j < n:
        while j<n:
            result.append(right[j])
            j+=1
    
    return result

print(merge([1,2,3,4,5],[0,6,7,8,9]))
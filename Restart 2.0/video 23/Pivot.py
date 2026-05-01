# To fine the pivot element
def partition(arr,low,high):
    i,j = low,high
    pivot = arr[low]
    while i<j:
        while arr[i] <= pivot and i <= high - 1:
            i += 1
        while arr[j] > pivot and j >= low + 1:
            j -= 1
        if i<j:
            arr[i],arr[j] = arr[j],arr[i]
    arr[j],arr[low] = arr[low],arr[j]
    return j

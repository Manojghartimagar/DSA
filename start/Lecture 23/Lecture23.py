from partition import partition

def Quick_Sort(nums,l,h):
    if l < h:
        p_index = partition(nums,l,h)
        Quick_Sort(nums,l,p_index-1)
        Quick_Sort(nums,p_index+1,h)

num = [1,6,9,2,4,9,10,5,7]
print(num)
Quick_Sort(num,0,len(num)-1)
print(num)
    
# tc = o(nlogn) sc = o(1) TC = o(N x N)


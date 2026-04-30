# Hashing in python -> prestoring values into some data structure like list sets dictionary and then fetching it from their.
n = [5,6,2,2,1,5,5,7,5,10] # n>=1 and n<=10
m = [10,111,1,9,5,6,7,2]
# brute force method TC = o(n*m) 
for i in m:
    count = 0
    for j in n:
        if i == j:
            count += 1
    print(f"{i} : {count}")
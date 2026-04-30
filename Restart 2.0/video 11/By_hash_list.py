n = [5,6,2,2,1,5,5,7,5,10] # n>=1 and n<=10
m = [10,111,1,9,5,6,7,2]

# another method TC = o(n + m) SC = o(10) == o(1)
hash_list = [0]*11
for i in n:
    if i in n:
        hash_list[i] += 1

for i in m:
    if i >= 1 and i <= 10:
        print(f"{i} : {hash_list[i]}")
    else:
        print(f"{i} : 0")
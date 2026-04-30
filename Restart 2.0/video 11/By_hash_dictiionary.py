n = [5,6,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,6,7,2]

hash_dict = {}
for i in n:
    hash_dict[i] = hash_dict.get(i,0) + 1

for num in m:
    if num in hash_dict:
        print(f"{num} : {hash_dict[num]}")
    else:
        print(f"{num} : 0")
#brute method

# n = [5,3,2,2,1,5,5,7,5,10]
# m = [10,111,1,9,5,67,2]
# dics = {}

# for i in m:
#     count = 0
#     for j in n:
#         if i == j:
#             count+=1
#     dics.setdefault(i,count)

# print(dics)

#TC = O(m*n) SC = O(1)


# n = [5,3,2,2,1,5,5,7,5,10]
# m = [10,111,1,9,5,67,2]

# hash_list = [0]*11

# for num in n:
#     hash_list[num]+=1

# for num in m:
#     if num <1 or num>10:
#         print(0)
#     else:
#         print(hash_list[num])

# TC = O(N+M) SC = O(1)

# n = [5,3,2,2,1,5,5,7,5,10]
# m = [10,111,1,9,5,67,2]

# hash_dics = {}
# for i in m:
#     hash_dics[i] = hash_dics.get(i,0) + 1

# for num in m:
#     if num not in hash_dics.keys():
#         hash_dics[num] = 0

# print(hash_dics)


s = "manjhfguosbgrtyeuido"
f =["g","m","f","y","u","r"]
hash_list = [0]*27

for ch in s:
    hash_list[ord(ch)-97] += 1

for ch in f:
    print(hash_list[ord(ch)-97])

hash_dics = {}
for ch in s:
    hash_dics[ord(ch)-97] = hash_dics.get(ord(ch)-97,0) + 1

print(hash_dics)
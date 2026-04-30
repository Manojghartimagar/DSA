s = "azyxyyzaass"
q = ["d","a","y","s","x"]

# method 1 TC = o(s*q)
for ch in q:
    count = 0
    for char in s:
        if ch == char:
            count += 1
    print(f"{ch} : {count}")

# method 2 TC = o(s + q) 
hash_list = [0]*26
for ch in s:
    ascii_value = ord(ch)
    index = ascii_value - 97
    hash_list[index] += 1

for ch in q:
    acsii_value = ord(ch)
    index = acsii_value - 97
    print(f"{ch} : {hash_list[index]}") 

# method 3 TC = o(m+n)
hash_map = {}
for ch in s:
    index = ord(ch) - 97
    hash_map[index] = hash_map.get(index,0) + 1

for ch in q:
    index = ord(ch) - 97
    if index in hash_map:
        print(f"{ch} : {hash_map[index]}")
    else:
        print(f"{ch} : 0")
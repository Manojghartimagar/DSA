def func(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return func(n-2) + func(n-1)
    

list = []
for i in range(0,11):
    list.append(func(i))

print(list)
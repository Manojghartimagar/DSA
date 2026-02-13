# def func(n,num):
#     if n != num+1:
#         print(n)
#         func(n+1,num)
#     else:
#         return
    
# num = int(input("Enter any number: "))
# func(1,num)

def func(num):
    if num != 0:
        func(num-1)
        print(num)
    else:
        return
    
num = int(input("Enter any number: "))
func(num)
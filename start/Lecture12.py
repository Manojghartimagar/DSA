# def func(count):
#     count = count-1
#     if (count == 0):
#         return
#     print("Manoj")
#     func(count)

# func(4) 

def func(count):
    count = count-1
    if (count == 0):
        return
    func(count)
    print("Manoj")

func(4) 


#TC = O(N) SC = O(N)
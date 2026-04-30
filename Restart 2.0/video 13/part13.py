# Recursion with parameters
def func(x,count):
    if count == 0:
        return 
    print(x)
    func(x,count-1)
func("Manoj",4)
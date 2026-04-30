# Recursion ->when function calls itself.it is also called stack.
# main two types of recursion 
# 1) head recursion
def func(count):
    if count == 4:
        return 
    print("Manoj")
    count += 1
    func(count)
func(0)

# 2) Tail Recursion
def func2(count):
    if count == 4:
        return 
    count += 1
    func(count)
    print("Manoj")

func2(0)

def rev_arr(num_arr:list,emp:list,i:int)-> list:
    if len(num_arr) != 0:
        emp.append(num.pop(len(num_arr)-1))
        return rev_arr(num_arr,emp,i+1)
    else:
        return emp

num = [5,7,3,2,6,1,5,9]
empty_num = rev_arr(num,[],0)
print(empty_num)




# num.reverse()
# # print(num.reverse())
# print(num)
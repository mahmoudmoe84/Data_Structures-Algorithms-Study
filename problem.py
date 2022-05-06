def fibonaccie (num):
    fibo_list = [0,1]
    
    if num == 0 :
        return num
    if num == 1 :
        return num
    while (len(fibo_list)-1) < num:
        fibo_list.append(fibo_list[-1]+fibo_list[-2])
    return fibo_list[num]

print(fibonaccie(1))


# Fn	Fibonacci Number
# 0	0
# 1	1
# 2	1
# 3	2
# 4	3
# 5	5
# 6	8
# 7	13
# 8	21
# 9	34

d   ef twosum(list_nums , target):
    for i in range(len(list_nums)):
        for j in range(i+1,len(list_nums)):
            if list_nums[i]+list_nums[j]==target:
                return i,j
nums =[2,5,5,11]
target = 10
print(twosum(nums,target))

# print("hello", end='')
# print("world", end='')
# 输出不换行

# print("i don't wanna")
# print("workallday")

# print("\ti\tdon't\twanna")
# print("\twork\tall\tday")

# i=1
# j=1
# while i <= 9:
#     while j <= i:
#         i += 1
#         print (j * i ,end='')

#定义外层循环的控制变量
i = 1
while i <= 9:

    #定义内层循环的控制变量
    j = 1                   #每次外循环开始时重置j
    while j <= i:
        #内层循环的print语句，不要换行. 通过\t制表符进行对齐
        print(f"{j} * {i} = {j * i}\t",end='')
        j += 1

    i += 1                  #放在内循环末尾，那么就只会运算一次；如果放在内循环的话就会生成两次
    print()
    #print空内容，就是输出一个换行



# i = 1
# while i <= 5:
#     j = 1
#     while j <= i:
#         print("*",end='')
#         j += 1
    
#     i += 1
#     print()


i = 9

while i <= 18:
    j = 9

    while j < i:
        print("阿弥托福",end='')
        j += 1
    i += 1
    print()
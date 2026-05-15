# continue ： 中断本次循环，直接进入下一次循环
#             可以用于for循环和while循环，效果一致

#continue 语句演示
# for i in range (1,7):
#     print("我真帅，我真聪明")

#     continue
#     print("也很有钱")

#continue 嵌套语句

# for i in range (1, 7):
#     print("yj1")
#     for j in range(1,7):
#         print("yj2")
#         continue
#         print("yj3")
    
# print("yj4")

"""
break 
结束循环
"""

for i in range (1,10):
    print("123")

    break
    print("456")
print("789")


for i in range(1,7):
    print("yj1")
    for j in range(1,7):
        print("yj2")

        break
        print("amtf")
    print("szsz")
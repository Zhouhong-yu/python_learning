# i = 0
# for i in range(1,101):
#     print(f"今天时向小妹表白的第{i}天")

#     for j in range(1,11):
#         print(f"给小妹送的第{j}朵茉莉花")

#     print("小妹我喜欢你")
# print(f"第{i}天，表白成功")

# i = 0 
# for i in range(1,101):
#     print(f"今天是给小妹表白的第{i}天")

#     j = 0
#     while j <= 10:
#         print(f"这是送给小妹的第{j}朵茉莉花")
#         j += 1
#     print("小妹我喜欢你")
# print(f"第{i}天，表白成功")

# i = 0
# while i <= 100:
#     print(f"今天是给小妹表白的第{i}天")

#     for j in range (1,11):
#         print(f"这是送给小妹的第{j}朵花")
    
#     i += 1
#     print("小妹我喜欢你")
# print(f"第{i - 1}天，表白成功")

for i in range(1,10):
    
    for j in range(1,i+1):                      #如果写range(1,10)，j永远从1到9，不管第几行都会打印9列
        print(f"{j} * {i} = {i*j}\t",end='')
    print()

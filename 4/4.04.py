#外层循环是表白100天
# #内层的循环是每天的表白送10只玫瑰花的控制

# i = 1                                       #i是外循环的控制变量
# while i <= 100:
#     print(f"今天是{i}天，准备.....")

#     #内层循环的控制变量
#     j = 1                                   #j是内循环的控制变量
#     while j <= 10:
#         print(f"送给xxx{j}支玫瑰花")
#         j += 1                              #作用于内循环，内层的条件

#     print ("xxx，我喜欢你")
#     i += 1                                  #作用于外循环，外层的条件
# print(f"坚持到第{i - 1}天，表白成功")

# #层数越多越复杂，越需要细心和耐心





day = 1
while day <= 52:
    print(f"今天是第{day}天，我喜欢你xxx")

    flower = 52

    while flower <= 52:
        print(f"我要送你{flower}朵玫瑰花")
        flower += 52

    day += 1
print("做我女朋友吧")
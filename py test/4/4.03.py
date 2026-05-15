
# import random
# num = random.randint(1,100)
# guess_time = 0
# while int(input("你猜一下呗：")) != num :
#     if int(input("你猜一下呗：")) < num :
#         print("猜大了")
#     else:
#         print("猜小了")

#     guess_time += 1 
# print(f"恭喜你猜对了，你一共猜了{guess_time}次")

# 获取范围在1-100的随机数字
import random
num = random.randint(1,100)

# 定义一个变量，记录总共猜测了多少次
count = 0

#通过一个布尔类型的变量，给循环是否继续的标记
# flag = True
# while flag:
#     guess_num = int(input("请输入你猜测的数字："))
#     count += 1
#     if guess_num == num :
#         print("猜中了")
#         #设置为False就是终止循环的条件
#         flag = False
#     else:
#         if guess_num > num :
#             print("你猜大了")
#         else:
#             print("你猜的小了")

# print(f"你总共猜测了{count}次")


import random
num = random.randint(1,100)

sum = 0;

time = True

while time :
    guess = int(input("请输入你要猜测的数字："))
    count += 1

    if guess == num:
        print("你猜对了，真棒")
    else:
        if guess > num:
            print("猜大了哦")
        else:
            print("猜小了哦")
    print(f"你一共猜了{count}次")
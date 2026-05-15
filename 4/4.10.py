# import random
# num = random.randint(1,10)
# money = 10000

# for i in range(1,21):
#     num = random.randint(1,10)
#     if num < 5:
#         print(f"员工{i}，绩效分{num}，低于5，不发工资，下一位")
#         continue

#     else:
#         money -= 1000
#         print(f"员工{i}，发放工资1000元，账户余额还剩余{money}元")

#         while True:
#             if money <= 0:
#                 print("工资发完了，下个月再来领吧")
#                 break
#             break

# print("本月工资发放结束")

money =100000

#for循环对员工发放工资
for i in range(1,21):
    import random
    score = random.randint(1,10)

    #if循环判断员工是否符合
    if score < 5:
        print(f"员工{i}，绩效分{score}，不满足。不发工资，下一位")
        #continue跳过发放
    
    #if循环判断公司余额是否足以发工资
    if money >= 10000:
        money -= 10000
        print(f"员工{i},满足条件发放工资10000元，公司账户余额{money}")
    else:
        print(f"余额不足，当前余额：{money}元，下个月再来")
        break   #结束循环
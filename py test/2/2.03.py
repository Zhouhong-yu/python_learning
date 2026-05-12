"""
    本段学习内容为变量
    变量就是再程序运行时，记录数据用的、存储数据用的
    记录数据是为了重复使用，而不是一直对这个值进行改动
"""
"""
# 定义一个变量，用来记录钱包的余额
money = 5488

# 通过print语句，输出变量记录的内容
print ("这个月的工资是：", money, "元")

# 买了一台电脑，花费7999元
pg = 7999
money = money - pg

print("买了电脑，还剩：", money, "元")

#假设，每隔一小时，输出一下钱包的余额
print("现在是下午一点，钱包余额：", money)
print("现在是下午二点，钱包余额：", money)
print("现在是下午三点，钱包余额：", money)
print("现在是下午四点，钱包余额：", money)
"""

#test

money = 50
print("钱包余额：",money)

icecream = 10
cola = 5

print ("购买了冰淇淋，花费：", icecream, "元")
print ("购买了可乐，花费：", cola, "元")

money = money - icecream -cola
print("最终，钱包剩余：", money, "元")
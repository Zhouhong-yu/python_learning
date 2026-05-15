#待处理数据集————序列类型
#指可以一个一个依次取出的一种类型包括：
# 字符串
# 列表
# 元组
# 等


"""
range语句
生成数字序列

语法一：range(5)                 依次
语法二：range(num1,num2)         从n1开始，不含n2本身
语法三：range(num1,num2,step)    n1开始，不包含n2本身，跳过step个数

"""
for x in range(10):
    print (x)

print()

for x in range (6 , 10):
    print(x)

print()

for x in range(6,18,4):
    print(x)



double = 0
for x in range(1,100):
    num = x % 2
    if num == 0:
        double += 1
print(f"句子里有{double}个偶数")  
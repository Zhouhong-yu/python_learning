"""
布尔类型的定义
比较运算符的应用

"""
#定义变量存储布尔类型的数据
ans_1 = True
ans_2 = False
print(f"ans_1的变量内容是：{ans_1}，类型是：{type(ans_1)}")
print(f"ans_1的变量内容是：{ans_2}，类型是：{type(ans_2)}")

#比较运算符的使用
# == ，！= ，>= , <= , < , >

num1 = 10
num2 = 10
print(f"10 == 10 的结果是：{num1 == num2}")

num1 = 10
num2 = 15
print(f"10 == 10 的结果是：{num1 != num2}")

name1 = "itcase"
name2 = "itbook"
print(f"itcase == itbook 结果是：{name1  == name2}")

#演示大于，小于， 大于等于，小于等于的比较运算
num1 = 10
num2 = 6
print(f"10 > 6 的结果是：{num1 > num2}")
print(f"10 < 6 的结果是：{num1 < num2}")

num1 = 10
num2 = 10
print(f"10 >= 10 的结果是：{num1 >= num2}")
print(f"10 <= 10 的结果是：{num1 <= num2}")

num1 = 10
num2 = 15
print(f"10 >= 15 的结果是：{num1 >= num2}")
print(f"10 <= 15 的结果是：{num1 <= num2}")
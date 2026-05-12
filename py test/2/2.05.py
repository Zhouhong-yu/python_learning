"""
    类型转换
    从文件中读取的数字默认是字符串类型，因此需要数据转换
    转换都有结果，因此可以使用变量去接受结果
"""

# 数字类型转换成字符串

num_str = str(13)
print(type(num_str),num_str)
# 不仅可以转换类型，而且还不会破坏内容


# 将字符串转换为数字
num = int("11")
print(type(num),num)

num2 = float(11.538)
print(type(num2),num2)

#想要将字符串转换成数字，必须要求字符串内的内容都是数字

#整数转浮点数
float_num = float(11)
print(type(float_num),float_num)

int_num = int(19.82)
print(type(int_num),int_num)
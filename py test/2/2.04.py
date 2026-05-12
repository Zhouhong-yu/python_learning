# 方法一：直接print输出变量存储结果
print(type("黑马程序员"))
print(type(666))
print(type(13.14))

#方法二： 使用变量存储type（）语句的结果
string_type = type("黑马程序员")
int_type = type(10)
float_type = type(13.14)
print(string_type)
print(int_type)
print(float_type)

# 方法三 使用type（）语句，查看变量中存储的数据类型信息
name = "周工，发工资啦"
name_type = type(name)
print(type(name))

"""
    变量存储数据；
    变量无类型，变量的数据有类型

    type（）语句会给出结果（返回值）
    
"""
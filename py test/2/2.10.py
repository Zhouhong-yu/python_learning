#字符串格式化

#通过占位的形式，完成拼接
name = "zhy"
message = "最帅、最聪明的是：%s" %name
print(message)


#通过占位的形式，完成数字和字符串的拼接
class_num = 15
avg_salary = 28500
message = "只要zhy好好学习%s年，就能够拿到%s的月薪，18薪" %(class_num,avg_salary)

print(message)

#   %表示：我要占位
#   s表示：我要占位的地方

name = "hyjt"
setup_year = 2031
stock_price = 39.56
message = "%s,成立于%d,今日股价:%f" %(name,setup_year,stock_price)
print(message)

"""
占位符：
字符串： %s
整数型： %d
浮点型： %f
"""
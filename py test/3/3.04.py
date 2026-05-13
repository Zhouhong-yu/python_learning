"""
else不需要判断条件
"""
print("欢迎来到欢乐谷，儿童免票，成人全票哦")

man = 80

age = input("你的年龄是：")
age = int(age)

#age = int(input("你的年龄是："))

if age >= 18 :
    print("sir , you need to buy the ticket")

else:
    print("sweethart~")

print("have a nice day!")
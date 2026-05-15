# for 临时变量 in 待处理数据集（序列）：
#       循环满足条件时执行的代码

#注意点：
#无法定义循环条件
#主语空格缩进

print("how to spell 'money'?")

word = "money"

for x in word:
    #将name 的内容，挨个取出赋予x临时变量
    #就可以在循环体内对x进行处理
    print(x)


sentence = "itheima is a brand of itcast"

a = 0

for x in sentence:
    

    if x == "a" :
        a += 1
print(f"句子里一共有{a}个a")
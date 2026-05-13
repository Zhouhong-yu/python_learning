num1 = 50

if int(input("请输入你想要猜的数字：")) == num1 :
    print("猜对了恭喜")

elif int(input("猜错了~再猜一次吧：")) == num1 :
    print("猜对了哦")

elif int(input("最后一次机会了哦：")) == num1 :
    print( " 终于猜对了！！！")

else :
    print("你全都猜错了，想要再来一次，请投币")

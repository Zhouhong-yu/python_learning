"""
嵌套判断语句
"""

if int(input("你的年龄是：")) > 18:
    print("恭喜你，你获得了参加本次活动的机会")

    if int(input("你在公司工作了_年")) > 1 :
        
        if int(input("你的职级是_")) > 3 :
            print("恭喜你获得了ipad一个")
        else :
            print("恭喜你获得保温杯一个")
    else :
        print("抱歉啊同事，你没有抽中奖品")
else :
    print("很遗憾，你没有参加本次活动的机会")
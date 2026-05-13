"""
判断是互斥且有顺序的
"""

money = int(input("你的股票价值是:"))
much = int(input("你的股票占总资产的百分之"))

if money >= 10000 :
    print("你需要谨慎一点")

elif much > 70 :
    print ("你需要降低持仓比例")
else :
    print("静待花开")




if int(input("你的股票价值是:")) >= 10000 :
    print("你需要谨慎一点")

elif int(input("你的股票占总资产的百分之")) > 70 :
    print ("你需要降低持仓比例")
else :
    print("静待花开")

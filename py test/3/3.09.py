import random
num = random.randint(1, 10)

guess = int(input("第一次，你猜这个数是："))
if guess > num:
    print("猜大了哦")
elif guess < num:
    print("猜小了哦")
else:
    print("你一次就猜对了，太棒了")
    exit()

guess = int(input("第二次，你猜这个数是："))
if guess > num:
    print("猜大了哦")
elif guess < num:
    print("猜小了哦")
else:
    print("真棒，第二次就猜对了")
    exit()

guess = int(input("第三次，你猜这个数是："))
if guess > num:
    print("还是猜大了，你没有机会了哦")
elif guess < num:
    print("还是猜小了，你没有机会了哦")
else:
    print("你终于猜对了")
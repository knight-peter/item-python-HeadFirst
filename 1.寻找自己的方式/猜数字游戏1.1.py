print("欢迎，这是一个猜数字游戏！")
guess=0#把要猜得的数字设为有效数字以确保循环会执行第一次
while guess!=5:#如果guess的值不对，程序就需要不停的运行。
    """下面那几行代码都缩进了，
    意味着它们属于循环体"""
    g=input("请输入一个数字：")
    guess=int(g)
    if guess==5:
        print("你猜对了！")
    else:
        if guess>5:
            print("太高了！")
        else:
            print("太低了！")
print("游戏结束！")
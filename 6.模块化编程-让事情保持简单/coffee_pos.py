# 这一行需要被加到任何使用“transactions.py”模块的程序中，“*”意味着“就像对待在你的程序中的代码那样对待模块中的代码”
from transactions import *# 添加记录模块
# 价格打折模块
import discount #去掉“from”和“*”后，需要使用模块名来限定函数名，例：discount.discount

# 这是包含菜单选项的数组
items=["甜甜圈","拿铁","松饼","美式咖啡","烤肠"]
# 这是菜单价格的对应数组
prices=[3.50,3.30,1.50,4.20,2.20]



running=True
while running:# 这个循环会一直惊喜，制药变量“running”的值为True。如果要结束循环，需要把“running”设为False
    option=1
    for choice in items:
        # 这部分代码显示程序的菜单。
        print(str(option)+"."+choice)# str()把数据类型转换成字符串
        option=option+1
    print(str(option)+".退出")
    # 用户输入一个菜单选项号码来点单
    choice=int(input("输入一个选项:"))# int()转换成正数
    # 如果用户选择了菜单上的最后一项，这个值就会是True
    if choice==option:# 这里的option是已经自增后的数值，相当于最后一个选项数值
        running=False
    else:
        credit_card=input("信用卡号码:")
        new_price=discount.discount(prices[choice-1],0.9)# new_price是打完折后的价格，调用discount()函数
        if input("你有健身房卡吗？（Y/N）")=="Y":
            new_price=discount.discount(new_price,0.95)
        save_transaction(new_price,credit_card,items[choice-1])
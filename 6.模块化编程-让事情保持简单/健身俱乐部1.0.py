'''
当Python看到一个字符串后面跟着一个百分号（%），它就知道它需要把这个字符串堪称一个字符串格式。
跟在%操作法后面的值将要以指定的顺序插入到格式化后的字符串中去，一次插一个值。
Python在字符串中没发现一个%，它就知道要插入一个值。

数字格式说明——%5d
当python看到这个，它就会把17这个值以5个字符长的数字形式插入——这是因为“d”这个类型说明符告诉Python把这个数字显示为一个十进制的数字。
因为17不是5个字符的长度，Python会在他的左边填充3个空格让它具有合适的长度。

字符串格式说明——%s
这个符号告诉Python把“巧克力口味”作为一个字符串插入。因为这儿你没有指明长度，字符串就以它本身的长度插入
'''


# "%s %e"%("Value is",16.0**0.5)                                  显示一个字符串，后面跟这4.000000e+00
# "%7d"%(11232/3)                                                 显示计算结果，并用空格填充
# # 如果只有一个值需要格式化，就不需要用圆括号把它围起来
# "%x"%127                                                        用16进制显示数字
# # \n意味着换行
# "%20s\n"%"Banana swirl"                                         把字符串填充到20位长，然后显示一个换行的
# # 这里的4意味着“使用4位字符”，这儿的2意味着“在小数点后显示2位数字”
# "%s is $%4.2f"%("Popsicle",1.754)                               和字符串一样，显示一个2位十进制的浮点数
# # 这儿的值可以是一个算数的结果
# "%s%f"%("Value is",16.0**0.5)                                   显示一个字符串，后面跟着4.000000
# # %后面的0意味着“用0填充”
# "%07d"%(11232/3)                                                显示使用0填充的值



# print("这里有%5d个%s甜甜圈"%(17,"巧克力口味"))

def save_transaction(price,credit_card,description):
    file=open("transactions.txt","a")# 这儿的“a”意味着你总是把记录添加在文件的尾部
    file.write("%16s%07d%s\n"%(credit_card,price*100,description))# 字符串格式说明——%s 数字格式说明——%5d
    file.close()

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
        save_transaction(prices[choice-1],credit_card,items[choice-1])
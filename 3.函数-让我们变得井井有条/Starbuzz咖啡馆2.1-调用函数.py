'''
import urllib.request
import time

price=99.99
while price>4.74:
    time.sleep(900)
    page=urllib.request.urlopen("http://www.ituring.com.cn/book")
    text=page.read().decode("utf8")
    where=text.find('>$')
    start_of_price=where+2
    end_of_price=start_of_price+4
    price=float(text[start_of_price:end_of_price])
print("Buy!")
'''


# 在函数里，你仍然需要在使用前导入库
import urllib.request
import time
# 函数的定义在这里开始，函数名后面需要加一个冒号
def get_price():
    # 函数主体代码需要缩进`
    page=urllib.request.urlopen("http://www.ituring.com.cn/book")
    text=page.read().decode("utf8")
    where=text.find('[作]')
    start_of_price=where+3
    end_of_price=start_of_price+7
    return(text[start_of_price:end_of_price])
#     函数定义结束
#调用函数前要先声明它


# 你需要询问用户是不是立即需要价格
price_now=input("你想看现在的价格吗？请输入‘Y’或者‘N’")
if price_now=="Y":
#     如果用户选择了“Y”，就把get_price()函数给你的值显示出来
    print(get_price())
else:
    # 如果用户选择等待价格下降，就通过get_price()函数拿到价格，然后用拿到的值来判断是不是买入咖啡豆的合适时机
    price=99.99
    while price>4.74:
        time.sleep(900)
        price=get_price()
    print("买！")




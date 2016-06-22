


# 在函数里，你仍然需要在使用前导入库
import urllib.request
import time

# 每一个函数都是一个新的堆栈帧，堆栈帧记录了一个函数里的创建的所有新变量。这些变量成为本地变量
'''
def set_password():
    password="password123456"
set_password()
'''
# 正确的做法
password="password123456"

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

# 代码中的msg变量需要变成函数的一个参数
def send_to_twitter(msg):
    # 这是需要发送的消息内容
    # msg="我要把这条消息发到微博上"
    password_manager=urllib.request.HTTPPasswordMgr()
    password_manager.add_password("Twitter API",
                                  "http://twitter.com/statuses","Twitter用户名",password)
    http_handler=urllib.request.HTTPBasicAuthHandler(password_mgr)
    page_opener=urllib.request.build_opener(http_handler)
    urllib.request.install_opener(page_opener)
    params=urllib.parse.urlencode({'status':msg})
    resp=urllib.request.urlopen("http://twitter.com/statuses/update.json",params)
    resp.read()


# 你需要询问用户是不是立即需要价格
price_now=input("你想看现在的价格吗？请输入‘Y’或者‘N’")
if price_now=="Y":
#     如果用户选择了“Y”，就把get_price()函数给你的值显示出来
    send_to_twitter(get_price())
else:
    # 如果用户选择等待价格下降，就通过get_price()函数拿到价格，然后用拿到的值来判断是不是买入咖啡豆的合适时机
    price=99.99
    while price>4.74:
        time.sleep(900)
        price=get_price()
    #     需要钱哦将调用print()替换成条用send_to_twitter
    send_to_twitter("Buy!")




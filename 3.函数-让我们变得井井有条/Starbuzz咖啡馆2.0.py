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


# 创建函数
def make_smoothie():
    juice=input("你喜欢什么饮料？")
    fruit=input("好的，然后你喜欢什么水果？")
    print("谢谢。开始吧！")
    print("加碎冰。。。")
    print("混合这种"+fruit)
    print("现在添加这种"+juice+"原浆")
    print("完成了！这是你要的"+fruit+"混合"+juice)



print("欢迎来混合果汁酒吧")
another="Y"
while another=="Y":
    # 调用这个函数
    make_smoothie()
    another=input("再来别的怎么样（Y/N）？")
print("欢迎下次光临！")
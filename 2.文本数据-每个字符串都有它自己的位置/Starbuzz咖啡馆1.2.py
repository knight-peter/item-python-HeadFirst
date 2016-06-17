'''
time.clock()    用秒来表示的当前时间，使用浮数点格式
time.daylight() 如果你当前不处在夏令时，就返回0
time.gmtime()   给出UTC时间的当前日期和时刻（不受你所在市区的影响）
time.localtime()给出当前本地时间（这会受你所在的时区的影响）
time.sleep(secs)在给定的秒数时间内休息，不做任何事
time.time()     给出从1970年1月1日算起到当前的秒数
time.timezone() 给出你所在的时区和UTC（伦敦）时区之间相差的小时数
'''


# 这段代码没有改变
import urllib.request
# 在程序的开头导入需要的库。这样做可以让程序访问该库所提供的所有内置函数
import time
price=99.99
while price>4.74:
    # 利用时间库函数的功能来使程序在两次请求之间暂停15分钟
    time.sleep(900)
    page = urllib.request.urlopen("http://www.ituring.com.cn/book")
    text=page.read().decode("utf8")
    where=text.find('>$')
    star_of_price=where+2
    end_of_price=star_of_price+4
    price=float(text[star_of_price:end_of_price])
print("Buy!")
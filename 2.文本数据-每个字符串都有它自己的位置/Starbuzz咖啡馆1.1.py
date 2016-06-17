'''
text.endswith(".jpg")                   如果字符串是以给定子字符串结尾的，就返回值true
text.upper()：                          返回一个被转换为全大写字母的字符串的副本
text.lower():                           返回一个被转换为全小写字母的字符串的副本
text.replace("tomorrow","Tuesday"):     返回一个字符串的副本，其中的某个子字符串全替换成另一个子字符串
text.strip():                           返回一个去除开空格和结尾空格的字符串副本
text.find("python"):                    当找到给定子字符串时，返回字符串的第一个字符串索引值
text.startswith("<HTML>")               如果字符串是以给定子字符串开头的，就返回值True
'''

# 这段代码没有改变
import urllib.request
# 给一个默认数字，让循环继续
price=99.99
while price>4.74:
    page = urllib.request.urlopen("http://www.ituring.com.cn/book")
    text=page.read().decode("utf8")
    # 搜索“>$”组合的索引位置
    where=text.find('>$')
    # 实际价格的起始位置是沿着字符串再后2位，而价格的结束则是起始位置的后4位
    start_of_price=where+2
    end_of_price=start_of_price+4
    # 在起始和结束索引位置已知的情况下，获得指定的子字符串很简单
    price=float(text[start_of_price:end_of_price])
# 你还记得找到价格后还要打印它吗
print("Buy!")
import urllib.request
page=urllib.request.urlopen("http://www.ituring.com.cn/book")
text=page.read().decode("utf8")
# text[14] 单个索引，只能得到一个单一字符
# 两个索引值，可以抽取一组字符，从第一个索引出的字符到第二个索引处之前的那个字符
price=text[234:238]
print(price)
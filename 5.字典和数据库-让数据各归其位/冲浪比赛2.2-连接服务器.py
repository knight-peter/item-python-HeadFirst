'''
# 编程工具
*哈希——一种把名字和数值关联起来的数据结构
*s['age']——从名为“s”的哈希中提取与“age”关联在一起的数值
*函数可以返回一个数据结构
*数据库系统——就像SQLite3的一种技术，可以搞笑存储大量数据
# Python 工具
*{}：一个空哈希
*s['wind']="off shore"——把“s”哈希中与“wind”相关联的数值设置为值“off shore”
*s.keys()——提供一个列表，包含名字为“s”的哈希中的所有关键字
*s.items()——提供一个列表，包含名为“s”的哈希中所有关键字和值
*line.split(",")——在每个逗号出现处分割包含包含在变量“line”中的字符串
*sorted()——一个内置函数，可以对很多数据结构排序
'''



import sqlite3

def find_details(id2find):
    # 从数据库中得到所有冲浪者的数据，而不是从文件中获取
    db=sqlite3.connect("surfersDB.sdb")
    db.row_factory=sqlite3.Row
    cursor=db.cursor()
    cursor.execute("select * from surfers")
    rows=cursor.fetchall()
    for row in rows:
        if row['id']==id2find
            s={}
            # 一次创建哈希的一个一值对
            s['id']=str(row['id'])
            s['name']=row['name']
            s['country']=row['country']
            s['average']=str(row['average'])
            s['board']=row['board']
            s['age']=str(row['age'])
            cursor.close()
            # 把哈希返回给调用代码
            return(s)
        cursor.close()
        return({})

'''
find_details(id2find)需要实现以下功能：
1.接受一个单一参数（冲浪者的ID）
2.每次处理数据文件中的一行，每次迭代用这行的信息生成一个哈希。
3.比较参数和文件中读取的ID
4.如果ID一致，就把哈希返回给调用代码。
5.如果没有找到一致的ID，就返回一个空的哈希
'''


def find_details(id2find):
    # 打开文件读取数据，python默认是ANSI格式
    surfers_f=open("surfing_data.txt")
    # 对文件的每一行使用for循环
    for each_line in surfers_f:
        # 确保哈希的初始值为空
        s={}
        # 把读取的行用split()分割后再把数据赋值给哈希
        (s['id'],s['name'],s['country'],s['average'],s['board'],s['age'])=each_line.split(";")
        # 检查参数提供的ID是否和文件中读取的ID一致
        if id2find==int(s['id']):
            surfers_f.close()
            return(s)# 如果找到一个相同的ID，关闭文件并返回当前的哈希给调用函数
    surfers_f.close()
    return({})# 没有找到相同的ID。所以，关闭文件并返回一个空的哈希


# 要求用户输入一个需要寻找的冲浪者ID
lookup_id=int(input("请输入冲浪者的ID："))
# 用输入的id做参数调用“find_details()”
surfer=find_details(lookup_id)
if surfer:
    print("ID:              "+surfer['id'])
    print("姓名：           "+surfer['name'])
    print("出生地：:        "+surfer['country'])
    print("成绩:            "+surfer['average'])
    print("参赛船型:        "+surfer['board'])
    print("年龄:            "+surfer['age'])


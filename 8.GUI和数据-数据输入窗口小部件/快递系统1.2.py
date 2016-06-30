# -*- conding: utf-8 -*-
'''
Entry()     用于输入单行文本
my_small_field=Entry(app)
my_small_field.get()                    #读取文本域的数据
my_small_field.insert(0,"banana")       #写入文本域的文档,0 是插入点的索引
my_small_field.delete(0,END)            #这将删除所有内容，0是域中第一个字符的索引。END是一个特殊值

Text()      用于更长的、多行文本
my_large_field=Text(app)
my_large_field.get("1.0",END)           #不像Entry(),你不能够仅仅使用get()来获取完整内容。"1.0"意味着从ROW=1和COLUMN=0，也就是域中的第一个字符——开始
my_large_field.delete("1.0",END)        #清空域
my_large_field.insert("1.0","Some text")#这将在域的起始位置插入文本

RadioButton(app,text="浙江杭州",value="浙江杭州") #单选框控件
'''
from tkinter import *
def save_data():
    fileD=open("deliveries.txt","a")
    fileD.write("仓库：\n")
    fileD.write("%s\n"%depot.get())
    fileD.write("描述：\n")
    fileD.write("%s\n"%description.get())
    fileD.write("地址：\n")
    fileD.write("%s\n"%address.get("1.0",END))
    # 存储数据后，清空所有文本域
    depot.set(None)
    description.delete(0,END)
    address.delete("1.0",END)

# 获取值添加到多选下拉框
def read_depos(file):
    depots=[]
#     打开文件
    depots_f=open(file)
    # 每次从文件中读取一行
    for line in depots_f:
        # 把去掉换行符后的行拷贝添加到数组里
        depots.append(line.rstrip())
    # 把列表返回给调用代码
    return depots

# 新建GUI标题
app = Tk()
app.title('快递详情')
# 新建label“仓库”和输入框
Label(app,text="仓库").pack()
depot=StringVar()# StringVar与IntVar类似，StringVar保存字符串，IntVar保存数字
depot.set(None)# 把depot设置成特殊值，“None”意思是没有值
# 调用函数，传入从中读取数据的文件的名称
options=read_depos("depots.txt")
# 使用数据来搭建选项菜单
OptionMenu(app,depot,*options).pack()

# 新建label“描述”和输入框
Label(app, text='描述:').pack()
description = Entry(app)
description.pack()
# 新建label“地址”和输入框
Label(app, text="地址：").pack()
address = Text(app)
address.pack()
# 新建button“保存”
Button(app, text="保存", command=save_data).pack()
# 开始tkinter事件的循环
app.mainloop()
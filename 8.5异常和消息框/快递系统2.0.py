# -*- conding: utf-8 -*-
'''
使用try和except来监控异常
tkinter.messagebox.showinfo("这里是消息框标题","这里是消息内容") # 消息框
showinfo            这是纯消息。没有什么好担心的。
showwarning         好，目前没有任何东西被毁，但是请小心
showerror           东西坏了，你需要知道
askquestion         你想要继续，但是你真的想要使用这个额外的选项吗
askokcancel         你真的确定你需要继续做这件事情？这是你可以改变注意的最后计划
askyesnocancel      你想要这个附加的选项，还是你希望忘掉证件事情
askretrycancel      上次它没有成功，但是如果你希望的话，你可以再试一次
'''
from tkinter import *
import tkinter.messagebox

def save_data():
    try:
        #try是异常处理标签
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
    # 这段代码任何地方抛出的一次都会让计算机跳转到这个位置
    # 在异常处理器中，异常被赋予了“ex”变量
    except Exception as ex:
        # 你需要使用showerror()函数，这样对话框有正确的错误图标
        tkinter.messagebox.showerror("错误","程序发生错误为： %s"%ex)

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
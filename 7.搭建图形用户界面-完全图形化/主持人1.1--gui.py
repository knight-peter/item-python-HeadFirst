'''
pack(side='left')       把按钮放置在窗口的左边
pack(side='right')      把按钮放置在窗口的右边
pack(side='top')        把按钮放置在窗口的顶端
pack(side='bottom')     把按钮放置在窗口的底部
pack(padex=10,pady=10)  在按钮的四周各留10个像素的空白部分
'''

# -*- conding: utf-8 -*-
# 从tkinter模块导入所有的功能
from tkinter import *

# 创建一个名为“app”的tkinter应用程序窗口
app=Tk()
# 给这个窗口起个名字
app.title("你的GUI窗口")
# 指定窗口的坐标和尺寸值,geometery('高度x宽度+X坐标+Y坐标')
app.geometry('450x100+200+100')
# 为“Correct”事件创建一个按钮
b1=Button(app,text="正确！",width=10)
# pack()方法把新创建的按钮链接到现有的窗口里
b1.pack(side='left',padx=10,pady=10)# 把一个按钮放置在左边

# 为“Wrong”事件创建另一个按钮
b2=Button(app,text="错误！",width=10)
b2.pack(side='right',padx=10,pady=10)# 把一个按钮放置在右边

# 开始tkinter的事件循环
app.mainloop()



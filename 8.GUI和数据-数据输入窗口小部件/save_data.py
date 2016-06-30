# -*- conding: utf-8 -*-
def save_data():
    fileD=open("deliveries.txt","a")
    fileD.write("仓库：\n")
    fileD.write("%s\n"%depot.get())
    fileD.write("描述：\n")
    fileD.write("%s\n"%description.get())
    fileD.write("地址：\n")
    fileD.write("%s\n"%address.get("1.0",END))
    depot.delete(0,END)
    description.delete(0,END)
    address.delete("1.0",END)
# # 打开的文件被赋予一个文件句柄，称为“result_f”
# result_f=open("results.txt")# 把要打开的文件的实际名称放在这里
#
# # 每次迭代都会把each_line变量设为文件的下一行。当所有的行读完时，for循环就停止了。
# for each_line in result_f:
#     # 用你从文件中读取的内容做些事情。在这个例子中，你打印了这一行。注意：for循环的代码是缩进的。
#     print(each_line)
# #     在你结束一个文件的处理时关闭这个文件（通过文件句柄）
# result_f.close()

highest_score=0
result_f=open("results.txt")
for line in result_f:
    # 添加split()方法的调用把文件中的行分割成两个字符串，创建"name"和"score"变量
    (name,score)=line.split()
    # 每次读到更高的分数时，highest_score变量都会被更新
    # 不再把一整行与最高分比较，现在比较的是变量"score"
    if float(score)>highest_score:
        # 记住要把字符串用float()转换成数字。尽管文件里的每一行都是数字，但它是作为一个字符串进入程序的
        highest_score=float(score)
result_f.close()
print("最好成绩是：")
print(highest_score)
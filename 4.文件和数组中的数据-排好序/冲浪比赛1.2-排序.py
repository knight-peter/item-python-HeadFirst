# count()     给出某个值在数组中出现的次数
# extend()    给数组增加一列元素
# index()     寻找一个数组元素并返回它的索引值
# insert()    在任意索引位置增加一个数组元素
# pop()       删除并返回最后一个数组元素
# remove()    删除并返回数组的第一个元素
# reverse()   把数组按相反的顺序排序
# sort()      用特定的顺序给数组排序（从低到高）



scores=[]
result_f=open("results.txt")
for line in result_f:
    # 添加split()方法的调用把文件中的行分割成两个字符串，创建"name"和"score"变量
    (name,score)=line.split()
    # score逐个添加到数组里
    scores.append(float(score))
result_f.close()# 代码运行到这儿时，数组已经在内存中了，但是它不是你需要的顺序。它没有顺序

scores.sort()
scores.reverse()
print(scores[0])
print(scores[1])
print(scores[2])
#!/usr/bin/python

#列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。

#举个例子，要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用range(1, 11)：
print range(1, 11)

#但如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环：
l = []
for x in range(1, 11):
    l.append(x * x)

print l


#但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list：
print [x * x for x in range(1, 11)]

#for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
print [x * x for x in range(1, 11) if x %2 == 0]


#还可以使用两层循环，可以生成全排列
print [m+n for m in "ABC" for n in "XYZ"]

#还可以使用三层循环
print [m+n+l for m in "ABC" for n in "XYZ" for l in "123"]


#列出当前目录下的所有文件和目录名，可以通过一行代码实现
import os
# # os.listdir可以列出文件和目录
print [d for d in os.listdir(".")]

#for循环其实可以同时使用两个甚至多个变量，比如dict的iteritems()可以同时迭代key和value：
d = {'x': "A", 'y': "B", 'z': "C"}
for k, v in d.iteritems() :
    print k, "=", v



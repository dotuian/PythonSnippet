#!/usr/bin/python

#如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，
#这种遍历我们称为迭代（Iteration）。

list = [12,5,34,5,34,23,4,23,4,63,45,4,765,7]
for n in list:
    print n


#因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样。
d = {"a": 1, "c": 3, "d": 4}
for key in d :
    print key

for value in d.itervalues():
    print value


for c in "ABCD":
    print c


#那么，如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：
from collections import Iterable
print isinstance('abc', Iterable) # str是否可迭代
print isinstance([1,2,3], Iterable) # list是否可迭代
print isinstance(123, Iterable) # 整数是否可迭代


#Python内置的enumerate函数可以把一个list变成索引-元素对，
#这样就可以在for循环中同时迭代索引和元素本身：

for index, value in enumerate(["a", "c", "e", "g"]) : 
    print index, value

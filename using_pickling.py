#!/usr/bin/python
# filename : using_pickling.py
# 对象的持久化与读取

#import..as语法。以便于我们可以使用更短的模块名称
import cPickle as p
#import pickle as p

shoplistfile = "shoplist.data"

shoplist = ["apple", "mango", "carrot"]

#write to file
f = file(shoplistfile, "w")
# dump the object to file
#dump函数，把对象储存到打开的文件中
p.dump(shoplist, f)
# close the file
f.close();

print shoplist

#remove the shoplist
del shoplist


# read back from file
f = file(shoplistfile)
#pickle模块的load函数的返回来取回对象
templist = p.load(f)
print templist


#!/usr/bin/python
# -*- coding: utf-8 -*-
#Filename: using_sys.py

#sys模块包含了与Python解释器和它的环境有关的函数。
import sys

print "The command line arguments are: "
for i in sys.argv:
    print i

print "\n\nThe Python Path is " , sys.path , "\n"

#每个Python模块都有它的__name__，如果它是'__main__'，这说明这个模块被用户单独运行
print __name__

#返回模块定义的名称列表

print dir(sys)
print dir()

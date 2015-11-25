#!/usr/bin/python
# -*- coding: utf-8 -*-
#Filename : ----.py


#不带参数的函数
def sayHello():
    print "Hello, World!"
sayHello()


#带参数的函数
def printMax(a, b):
    if a > b:
        print a, "is maximum"
    else:
        print b, "is maximum"

printMax(3,4)
printMax(6,4)


#使用global声明全局变量
def func():
    global x
    print "x is", x
    x = 2
    print "change x to", x

x = 50
func()
print "Value of x is", x


#使用默认参数
def say(message, times=2):
    index = 0
    while index < times :
        print message
        index = index + 1

say("Hello,World")
print "---------"
say("Hello,World", 3)


#关键参数
def func1(a, b=5, c=10):
    print "a is", a, "b is", b, "c is", c

func1(3,4)
func1(25, c=20)
func1(c=50,a=100)

# return语句
def maximum(x, y) :
    if x > y :
        return x
    else:
        return y

print maximum(19,20)
print maximum(19,2)


# 文档字符串
def printMax(x, y):
    """Prints the maximum of two numbers.
The Two values must be integers"""
    x =int(x)
      y=int(y)

    if x > y :
        print x,"is maximum"
    else:
        print y,"is maximum"

printMax(3,5)
print printMax.__doc__













#!/usr/bin/python


#变量可以指向函数
print abs(-10)
f = abs
print f(-10)


#一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。

def add(x, y, f):
    return f(x) + f(y)

print add(-9, -10, abs)

#Python内建了map()和reduce()函数。
#map()函数接收两个参数，一个是函数，一个是序列，
#map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回。

def f2(x):
    return x * x
print map(f2, [0, 1,2,3,4,5,6,7,8,9])
print map(f2, [x for x in range(10)])
print map(f2, range(10))



#reduce把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数，
#reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
def add(x, y):
    return x + y
# 1+2+3+...+9
print reduce(add, range(10))

def f3(x,y):
    return x * 10 + y
print reduce(f3, range(10))


#str转换为int的函数
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
print reduce(f3, map(char2num, "5698"))

#int转换为str的函数
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))

print str2int("1234")

#用lambda函数进一步简化成
def char2num(s):
    #去字典中对应的键值
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2int(s):
    return reduce(lambda x,y: x*10+y, map(char2num, s))

print char2num("0")
print str2int("12343534")


#过滤
def isOdd(n):
    return n % 2 == 0
print filter(isOdd, range(20))

def notEmpty(s):
    return s and s.strip()
print filter(notEmpty, ["A", "B", None, " ", "E"])


#排序
lst = [3,46,23,23,43,12]
print (lst)

def fCmp(x, y) :
    if x > y:
        return -1
    if x <y :
        return 1
    return 0

print sorted(lst, fCmp)

print sorted(['bob', 'about', 'Zoo', 'Credit'])


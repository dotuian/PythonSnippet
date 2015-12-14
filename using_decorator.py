#!/usr/bin/python

#decorator可以增强函数的功能，定义起来虽然有点复杂，但使用起来非常灵活和方便。



def now():
    print "now time"

f = now
f()

#函数对象有一个__name__属性，可以拿到函数的名字：
print now.__name__
print f.__name__

#假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
#这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）


#wrapper()函数的参数定义是(*args, **kw)，因此，
#wrapper()函数可以接受任意参数的调用。在wrapper()函数内，首先打印日志，
#再紧接着调用原始函数。

def log(func):
    def wrapper(*agrs, **kw):
        print "call %s" % func.__name__
        return func(*agrs, **kw)
    return wrapper

@log
def showTime():
    print "show time"

showTime()

#int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换：
print int('12345')

#但int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换：
print int('12345', base=8)
print int('12345', 16)

def int2(x, base=2):
    return int(x, base)

print int2('1000000')
print int2('1010101')

#functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，
#可以直接使用下面的代码创建一个新的函数int2：
import functools
int2 = functools.partial(int, base=2)
print int2('1000000')
print int2('1010101')

#functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），
#返回一个新的函数，调用这个新函数会更简单。















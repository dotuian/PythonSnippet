
class MathTest:
    """ this is a test math class"""
    
    def fact(self, n) :
        if n==1:
            return 1
        return n * self.fact(n-1)

m = MathTest();
print m.fact(4)

    

#pass语句什么都不做，那有什么用？
#实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，
#就可以先放一个pass，让代码能运行起来。
def nop():
    pass
nop()

#缺少了pass，代码运行就会有语法错误。
age = 19
if age > 10 :
    pass

#通过tuple返回多个值
def addone(x, y):
    return x+1, y+1

x, y = addone(3,9)
print x
print y
print addone(4,5)



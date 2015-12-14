#!/usr/bin/python

class Student:
    """ this is a test class """
    def __init__(self, name, score):
        self.name = name
        self.__score = score

    def info(self):
        print "name: %s score:%s " %(self.name, self.__score)

s = Student("zhong", 99)
print s.__doc__
s.info()


s.name = "test"
s.score = 100
s.info()

#判断一个变量是否是某个类型可以用isinstance()判断：
print isinstance(s, Student)

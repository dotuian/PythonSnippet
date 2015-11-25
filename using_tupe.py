# -*- coding: utf-8 -*-
#using_tupe.py

zoo = ("wolf", "elephant", "penguin")
print "Number of animals in the zoo is", len(zoo)

new_zoo = ("monkey", "dolphin", zoo)
print "Number of animals in the new zoo is", len(new_zoo)

print "All animals in new zoo are", new_zoo

print "Animals brought from old zoo are", new_zoo[2]
print "Last animals brought from old zoo is ", new_zoo[2][2]


age = 22
name = "swift"

# %s表示字符串
# %d表示整数
#print语句可以使用跟着%符号的项目元组的字符串
print "%s is %d years old" %(name, age)

#!/usr/bin/python
# _*_ charset: uff-8 _*_


array = [1,2,3]
s = set(array)
print s

array = [1,2,3, 3, 3, 4]
s = set(array)
print s

#通过add(key)方法可以添加元素到set中,可以重复添加，但不会有效果：
s.add(4)
print s

s.add(5)
print s

#通过remove(key)方法可以删除元素
s.remove(4)
print s

#set可以看成数学意义上的无序和无重复元素的集合，
#因此，两个set可以做数学意义上的交集、并集等操作：
s1 = set([1,2,3,4])
s2 = set([3,4,5,6])
#交集
print s1 & s2

#并集
print s1 | s2


s = [3,4,1,5,9,7]
#数组排序
s.sort();
print s





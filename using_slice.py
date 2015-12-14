#!/usr/bin/python
# _*_ charset: utf-8 _*_

l = ["a", "b", "c", "d"]
print l
print [l[0], l[1], l[2]]

r = []
n = 3
for i in range(n) :
    r.append(l[i])
print r

#指定索引范围的操作，用循环十分繁琐，
#因此，Python提供了切片（Slice）操作符，能大大简化这种操作。
# l[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。
print l[0:3] 


#如果第一个索引是0，还可以省略：
print l[:3]

#也可以从索引1开始，取出2个元素出来：
print l[1:3]

#Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片
print l[-2:]

l = range(100)
print l

#前10个数
print l[:10]

#后10个数
print l[-10:]

#前11-20个数
print l[10:20]

#前10个数，每两个取一个
print l[:10:2]

#所有数，每5个取一个：
print l[::5]

#甚至什么都不写，只写[:]就可以原样复制一个list：
print l[:]

#tuple也是一种list，唯一区别是tuple不可变。
#因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
print (0,1,2,3,4,5)[:3]


#字符串'xxx'或Unicode字符串u'xxx'也可以看成是一种list，
#每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：
print "我是中国人！"[0:3]

print "ABCDEFG"[0:3]
















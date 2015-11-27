#!/usr/bin/python
# filename : using_exception.py

#使用try..except语句来处理异常
#把通常的语句放在try-块中，而把我们的错误处理语句放在except-块中。


import sys

try:
    s = raw_input("Enter something --> ")
except EOFError:
    print "\n Why did you do a EOF on me ? "
    # exit the program
    sys.exit();
    
except:
    print "\nSome error/exception occurred."

print "Done"   


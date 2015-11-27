#!/usr/bin/python
#filename : using_raising.py
#自定义异常
import sys

class ShortInputException(Exception):
    """ A user-defined exception class. """

    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast




try:
    s = raw_input("Enter something -->>> ")
    if len(s) < 3 :
        #可以使用raise语句抛出异常
        raise ShortInputException(len(s), 3)

except EOFError:
    print "\n Why did you do a EOF on me ? "
    # exit the program
    sys.exit();
    
except ShortInputException, x:
    print "ShortInputException: The input was of length %d \
was expecting at least %d" % (x.length, x.atleast)
    sys.exit();
    
else:
    print "No exception was raised"

#/usr/bin/python
# filename : using_file_io.py

#模式可以为读模式（'r'）、写模式（'w'）或追加模式（'a'）


poem ="""\
Programming is fun
when the work is done


if you wanna make your work also fun use Python !
"""

# open for writing
f = file("test.txt", "a")

# write text to file
f.write(poem)

# close the file
f.close();

# if no mode is specified, read mode is assumed by default
f = file("test.txt")

while True:
    line = f.readline()
    # zero length indicates EOF
    if len(line) == 0 :
        break
    print len(line), line

# close the file
f.close()

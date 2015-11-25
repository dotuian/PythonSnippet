#!/usr/bin/python
# -*- coding: utf-8 -*-
#Filename: controll.py

number = 23
running = True

while running :
    guess = int(raw_input("Enter an integer : "))

    if guess == number :
        print "OK"
        running = False
    elif guess < number :
        print "too samll"
    else :
        print "to big"
else:
    print "The while loop is over."

print "Done"


for i in range(1, 5) :
    print i
else : 
    print "The for loop is over"


while True:
    s = raw_input("Enter something:")
    if s == "quit":
        break
    if len(s) < 3 :
        continue
    print "Input is of sufficient lenght "
    

#!/usr/bin/python
# -*- coding: utf-8 -*-
# filename: using_class.py

class Person:

    """ Represents a person """

    population = 0

    #构造函数
    def __init__(self, name):
        """ Initializes the person's data. """
        self.name = name
        print "Initializing %s" %self.name

        # When this person is created, he/she
        # adds to the population
        Person.population += 1

    #析构函数
    def __del__(self):
        """ I am dying. """
        print "%s say bye . " %self.name

        Person.population -= 1

        if Person.population == 0:
            print "I am the last one"
        else :
            print "There are still %d people left" %Person.population
    
    def sayHi(self):
        """ Gretting by the person """
        print "Hello, how are you!", self.name

    def howMany(self):
        """ Prints the current population. """
        if Person.population == 1 :
            print "I am the only person here."
        else:
            print "We have %d persons here. " % Person.population
    
p1 = Person("zhong");
p1.sayHi()
p1.howMany()

p2 = Person("kayi");
p2.sayHi()
p2.howMany()

del p2



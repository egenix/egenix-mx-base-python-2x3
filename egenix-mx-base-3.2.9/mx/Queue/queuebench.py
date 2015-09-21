#!/usr/local/bin/python -O
""" queuebench - queue implementation benchmark

    Copyright (c) 2000, Marc-Andre Lemburg; mailto:mal@lemburg.com
    Copyright (c) 2000-2015, eGenix.com Software GmbH; mailto:info@egenix.com
    See the documentation for further information on copyrights,
    or contact the author. All Rights Reserved.
"""
import time
from mx import Queue
import UserQueue
from sys import argv, exit

try:
    numtests, pushes, pops = eval(argv[1]), eval(argv[2]), eval(argv[3])
    assert pushes >= pops
except:
    print 'usage: queuebench.py <ntests> <pushes> <pops>, where <pushes> >= <pops>'
    exit(1)
 
def test(reps, func):
    start_cpu  = time.clock()
    for i in xrange(reps):
        x = func()
    return time.clock() - start_cpu
 
def method1():
    x = []                                           # built-in list
    push = x.append
    for i in range(pushes): push('spam'+'i')
    for i in range(pops):   top = x[0]; del x[0]

def method3():
    s = Queue.Queue()                              # Queue
    push = s.push
    pop = s.pop
    for i in range(pushes): push('spam'+'i')
    for i in range(pops):   top = pop()

if 0:
    def method3a():
        s = Queue.Queue()                              # Queue
        push = s.push
        for i in range(pushes): push('spam'+'i')
        t = s.pop_many(pops)                             # pop all at once

def method3b():
    s = Queue.Queue()                              # Queue
    push = s.push
    for i in range(pushes): s << ('spam'+'i')
    for i in range(pops):   top = s >> 1

if 0:
    def method3c():
        s = Queue.Queue()                              # Queue
        l = [''] * pushes
        for i in range(pushes): l[i] = ('spam'+'i')
        s.push_many(l)
        s.pop_many(pops)

def method4():
    s = UserQueue.UserQueue()                         # UserQueue
    push = s.push
    pop = s.pop
    for i in range(pushes): push('spam'+'i')
    for i in range(pops):   top = pop()

print 'list: ', test(numtests, method1)            # run func 20 tests
print 'Queue (with push + pop):', test(numtests, method3)
#print 'Queue (with push + pop_many):', test(numtests, method3a)
print 'Queue (with << + >>):', test(numtests, method3b)
#print 'Queue (with push_many + pop_many):', test(numtests, method3c)
print 'UserQueue:', test(numtests, method4)
 


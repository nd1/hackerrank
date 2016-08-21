#!/bin/python

import sys


N = int(raw_input().strip())

if N%2 == 1:
    print "Weird"
elif N in range(6,21):
    print "Weird"
else:
    print "Not Weird"
       

#!/bin/python3

import sys


N = int(input().strip())
for x in range(1,11):
    print ("%d x %d = %d" % (N, x, N*x))

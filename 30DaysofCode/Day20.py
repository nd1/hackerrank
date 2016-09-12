#!/bin/python3

import sys


n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
numSwaps = 0

for pass_num in range((n-1), 0, -1):
    for i in range(pass_num):
        if a[i]>a[i+1]:
            temp = a[i]
            a[i] = a[i+1]
            a[i+1] = temp
            numSwaps += 1

print("Array is sorted in {!s} swaps.".format(numSwaps))
print("First Element: {!s}".format(a[0]))
print("Last Element: {!s}".format(a[-1]))

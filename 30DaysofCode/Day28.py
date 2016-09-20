#!/bin/python3
import re
import sys

lst = []
N = int(input().strip())
for a0 in range(N):
    firstName, emailID = input().strip().split(' ')
    firstName, emailID = [str(firstName), str(emailID)]
    if re.search('@gmail\.com$', emailID):
        lst.append(firstName)

print(*sorted(lst), sep='\n')

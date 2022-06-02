#!/usr/bin/python
def uppercase(str):
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            c = chr(ord(c) - (ord('a') - ord('A')))
            print("{:s}".fomrat(c), end='')
        print("")

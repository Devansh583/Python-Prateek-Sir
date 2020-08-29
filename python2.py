#program of Hello World
print('Hello, World!')

#program of if-else statement
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

if n%2 == 0:
    if n in range(2,6):
        print('Not Weird')
    elif n in range(6,21):
        print('Weird')
    elif n >20:
        print('Not Weird')
        
elif n%2 != 0:
        print('Weird')

#program of arithmetic operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())

print(a+b)
print(a-b)
print(a*b)

#program for division
if __name__ == '__main__':
    a = int(input())
    b = int(input())

print(a//b)
print(a/b)

#program of loop
if __name__ == '__main__':
    n = int(input())

for i in range(0,n):
    print(i**2)

#!/bin/python3

import math
import os
import random
import re
import sys
#multiplier problem from HackerRank
def multiply(m):
    for i in range(1,11):
        print(m,'x',i,'=',m*i)
if __name__ == '__main__':
    n = int(input())
    multiply(n)
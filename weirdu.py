#!/bin/python3

import math
import os
import random
import re
import sys


def weirdu(n):
    if (n % 2) != 0:
        print('Weird')
    else:
        if (n >= 2 and n <= 5) or (n > 20):
            print(n)
            print('Not Weird')
        else:
            print('Weird')


if __name__ == '__main__':
    N = int(input())
    weirdu(N)


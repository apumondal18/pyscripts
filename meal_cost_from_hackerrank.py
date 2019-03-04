#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    meal_cost_1 = meal_cost + (meal_cost*float(tip_percent)/100)
    meal_cost_2 = meal_cost_1 + (meal_cost*float(tax_percent)/100)
    print(round(meal_cost_2))

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)

#!/usr/bin/python3

import sys
from math import sqrt

total_sum = 0

# input = open('output.txt', 'r')
# output = open('norm.txt', 'w')

for line in sys.stdin:
    line = line.strip()

    sum = line.split('\t')

    total_sum += float(sum[1])

# emit -> norm (norm is a sqrt value of the sum from mapper)
print(f'norm\t{round(sqrt(total_sum), 2)}')

# input.close()
# output.close()

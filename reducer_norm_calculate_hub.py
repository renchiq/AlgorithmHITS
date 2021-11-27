#!/usr/bin/python3

import sys
import redis
from math import sqrt

total_sum = 0
r = redis.Redis()

# input = open('output.txt', 'r')
# output = open('norm.txt', 'w')

for line in sys.stdin:
    line = line.strip()

    sum = line.split('\t')

    total_sum += float(sum[1])

# emit -> norm (norm is a sqrt value of the sum from mapper)
r.mset({'hubnorm': str(round(sqrt(total_sum), 2))})
print(f'norm\t{round(sqrt(total_sum), 2)}')

# input.close()
# output.close()

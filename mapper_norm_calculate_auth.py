#!/usr/bin/python3

import sys

total_sum = 0

# input = open('input3.txt', 'r')
# output = open('output.txt', 'w')

for line in sys.stdin:
    line = line.strip()

    page, page_auth_score, page_hub_score, adjacency_lis = line.split('\t')

    total_sum += float(page_auth_score) ** 2

# emit -> sum (next step sqrt of this sum)
print(f'sum\t{round(total_sum, 4)}')

# input.close()
# output.close()

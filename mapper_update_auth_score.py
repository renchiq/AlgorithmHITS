#!/usr/bin/python3

import sys

# input = open('input2.txt', 'r')
# output = open('output.txt', 'w')

for line in sys.stdin:
    line = line.strip()

    page, page_auth_score, page_hub_score, adjacency_list = line.split('\t')

    adj_pages = adjacency_list.split(',')

    # emit -> node_name | auth | hub
    # output.write(f'{page}\t{page_auth_score}\t{page_hub_score}\n')
    print(f'{page}\t{page_auth_score}\t{page_hub_score}')

    for adj_page in adj_pages:
        # emit -> adj_page | node_name | hub
        # output.write(f'{adj_page}\t{page}\t{round(float(page_hub_score) / len(adj_pages), 2)}\n')
        print(f'{adj_page}\t{page}\t{round(float(page_hub_score) / len(adj_pages), 2)}')

# input.close()
# output.close()

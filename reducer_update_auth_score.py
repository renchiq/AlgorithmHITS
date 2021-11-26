#!/usr/bin/python3

import sys
from collections import defaultdict

latest_link = None
latest_score = [0, 0]
latest_sources = []

# input = open('output.txt', 'r')
# output = open('input3.txt', 'w')

for line in sys.stdin:
    # for line in file:
    line = line.strip()

    link, value, auth_score = line.split('\t')

    if latest_link is not None and latest_link != link:
        # emit -> page | auth score | hub score | adjacency list
        # output.write(f'{latest_link}\t{latest_score[0]}\t{latest_score[1]}\t{",".join(map(str, latest_sources))}\n')
        print(f'{latest_link}\t{latest_score[0]}\t{latest_score[1]}\t{",".join(map(str, latest_sources))}')

        latest_link = link
        latest_score = [0, 0]
        latest_sources.clear()

        if value.isnumeric():
            latest_score[1] = auth_score
        else:
            latest_sources.append(value)

            latest_score[0] += float(auth_score)
    else:
        if latest_link is None:
            latest_link = link

        if value.isnumeric():
            latest_score[1] = auth_score
        else:
            latest_sources.append(value)

            latest_score[0] += float(auth_score)

# emit -> page | auth score | hub score | adjacency list
# output.write(f'{latest_link}\t{latest_score[0]}\t{latest_score[1]}\t{",".join(map(str, latest_sources))}\n')
print(f'{latest_link}\t{latest_score[0]}\t{latest_score[1]}\t{",".join(map(str, latest_sources))}')

# input.close()
# output.close()

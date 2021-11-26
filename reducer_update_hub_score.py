#!/usr/bin/python3

import sys

latest_source = None
latest_score = [0, 0]
latest_sources = []

# input = open('output.txt', 'r')
# output = open('input2.txt', 'w')

for line in sys.stdin:
    line = line.strip()

    source, value, hub_score = line.split('\t')

    if latest_source is not None and latest_source != source:
        # emit -> page | auth score | hub score | adjacency list
        # output.write(f'{latest_source}\t{latest_score[0]}\t{latest_score[1]}\t{",".join(map(str, latest_sources))}\n')
        print(f'{latest_source}\t{latest_score[0]}\t{latest_score[1]}\t{",".join(map(str, latest_sources))}')

        latest_source = source
        latest_score = [0, 0]
        latest_sources.clear()

        if value.isnumeric():
            latest_score[0] = value
        else:
            latest_sources.append(value)
            latest_score[1] += float(hub_score)
    else:
        if latest_source is None:
            latest_source = source

        if value.isnumeric():
            latest_score[0] = value
        else:
            latest_sources.append(value)
            latest_score[1] += float(hub_score)

# emit -> page | auth score | hub score | adjacency list
# output.write(f'{latest_source}\t{latest_score[0]}\t{latest_score[1]}\t{",".join(map(str, latest_sources))}\n')
print(f'{latest_source}\t{latest_score[0]}\t{latest_score[1]}\t{",".join(map(str, latest_sources))}')

# input.close()
# output.close()

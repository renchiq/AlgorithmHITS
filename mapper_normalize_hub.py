#!/usr/bin/python3

import sys
import pyhdfs

fs = pyhdfs.HdfsClient(hosts='localhost:50070', user_name='renchiq-centos')

with fs.open("/user/renchiq-centos/hits/results/hub-sum-total/part-00000") as f:
    lines = [x.decode('utf8').strip() for x in f.readlines()]
    norm = float(lines[0].strip().split('\t')[1])

for line in sys.stdin:
    line = line.strip()

    page, page_auth_score, page_hub_score, adjacency_list = line.split('\t')

    print(f'{page}\t{page_auth_score}\t{round(float(page_hub_score) / norm, 2)}\t{adjacency_list}')

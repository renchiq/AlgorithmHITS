#!/usr/bin/python3

import sys
import pyhdfs
import redis

fs = pyhdfs.HdfsClient(hosts='localhost:50070', user_name='renchiq-centos')
r = redis.Redis()

# counter = 1
# if r.get('hub') is None:
#     r.mset({'hub': str(counter)})
# else:
#     counter = int(r.get('hub').decode("utf-8"))
#     r.mset({'hub': str(counter + 1)})

# with fs.open(f"/user/renchiq-centos/hits/results/{counter}/hub-sum-total/part-00000") as f:
#     lines = [x.decode('utf8').strip() for x in f.readlines()]
#     norm = float(lines[0].strip().split('\t')[1])

norm = float(r.get('hubnorm').decode("utf-8"))

for line in sys.stdin:
    line = line.strip()

    page, page_auth_score, page_hub_score, adjacency_list = line.split('\t')

    print(f'{page}\t{page_auth_score}\t{round(float(page_hub_score) / norm, 2)}\t{adjacency_list}')

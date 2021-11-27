#!/usr/bin/python3

import sys
import pyhdfs
import redis

fs = pyhdfs.HdfsClient(hosts='localhost:50070', user_name='renchiq-centos')
r = redis.Redis()

# counter = 1
# if r.get('auth') is None:
#     r.mset({'auth': str(counter)})
# else:
#     counter = int(r.get('auth').decode("utf-8"))
#     r.mset({'auth': str(counter + 1)})
#
# with fs.open(f"/user/renchiq-centos/hits/results/{counter}/auth-sum-total/part-00000") as f:
#     lines = [x.decode('utf8').strip() for x in f.readlines()]
#     norm = float(lines[0].strip().split('\t')[1])

norm = float(r.get('authnorm').decode("utf-8"))

for line in sys.stdin:
    line = line.strip()

    page, page_auth_score, page_hub_score, adjacency_list = line.split('\t')

    print(f'{page}\t{round(float(page_auth_score) / norm, 2)}\t{page_hub_score}\t{adjacency_list}')

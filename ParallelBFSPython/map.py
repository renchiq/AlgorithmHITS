#!/usr/bin/python3
import sys

for line in sys.stdin:
    kv = line.strip().split("\t")
    node_id = kv[0]
    value_list = kv[1].split(";")
    d = int(value_list[0])
    links = value_list[1].split(" ")
    line = line.replace("\n", "")
    for m in links:
        print(m + "\t" + str(d+1))
    print(line)

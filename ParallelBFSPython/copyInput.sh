#!/bin/bash

hdfs dfs -mkdir PBFS
hdfs dfs -mkdir PBFS/itr_1

hdfs dfs -put input.txt PBFS/itr_1

#!/bin/bash

hdfs dfs -rm -r hits

hdfs dfs -mkdir hits
hdfs dfs -mkdir hits/input
hdfs dfs -mkdir hits/input/0

hdfs dfs -put dataset.txt hits/input/0
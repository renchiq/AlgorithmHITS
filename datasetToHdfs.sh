#!/bin/bash

hdfs dfs -mkdir hits
hdfs dfs -mkdir hits/input

hdfs dfs -put dataset.txt hits/input
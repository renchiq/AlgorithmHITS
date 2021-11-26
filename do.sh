#!/bin/bash
iterations=3

for ((itr=1; itr <= iterations; itr++)); do
  hdfs dfs -rm -r hits/results

  yarn jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -D mapreduce.job.name="HITS Hub Score Update | Job via Streaming" \
  -files `pwd`/mapper_update_hub_score.py,`pwd`/reducer_update_hub_score.py \
  -input hits/input \
  -output hits/results/hub \
  -mapper `pwd`/mapper_update_hub_score.py \
  -reducer `pwd`/reducer_update_hub_score.py

  yarn jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -D mapreduce.job.name="HITS Auth Score Update | Job via Streaming" \
  -files `pwd`/mapper_update_auth_score.py,`pwd`/reducer_update_auth_score.py \
  -input hits/results/hub \
  -output hits/results/authority \
  -mapper `pwd`/mapper_update_auth_score.py \
  -reducer `pwd`/reducer_update_auth_score.py


  yarn jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -D mapreduce.job.name="HITS Hub Sum Calculate | Job via Streaming" \
  -files `pwd`/mapper_norm_calculate_hub.py,`pwd`/reducer_norm_calculate_hub.py \
  -input hits/results/authority \
  -output hits/results/hub-sum-total \
  -mapper `pwd`/mapper_norm_calculate_hub.py \
  -reducer `pwd`/reducer_norm_calculate_hub.py


  yarn jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -D mapreduce.job.name="HITS Hub Normalization | Job via Streaming" \
  -files `pwd`/mapper_normalize_hub.py \
  -input hits/results/authority \
  -output hits/results/hub-normalization-result \
  -mapper `pwd`/mapper_normalize_hub.py


  yarn jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -D mapreduce.job.name="HITS Auth Sum Calculate | Job via Streaming" \
  -files `pwd`/mapper_norm_calculate_auth.py,`pwd`/reducer_norm_calculate_auth.py \
  -input hits/results/hub-normalization-result \
  -output hits/results/auth-sum-total \
  -mapper `pwd`/mapper_norm_calculate_auth.py \
  -reducer `pwd`/reducer_norm_calculate_auth.py

  hdfs dfs -rm -r hits/input

  yarn jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -D mapreduce.job.name="HITS Auth Normalization | Job via Streaming" \
  -files `pwd`/mapper_normalize_auth.py \
  -input hits/results/hub-normalization-result \
  -output hits/input/ \
  -mapper `pwd`/mapper_normalize_auth.py
done
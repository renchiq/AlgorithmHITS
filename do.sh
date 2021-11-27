#!/bin/bash

redis-cli flushdb

iterations=3

for ((itr=1; itr <= iterations; itr++)); do
  # 1 Обновление посредников
  yarn jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -D mapreduce.job.name="HITS Hub Score Update | Job via Streaming" \
  -files `pwd`/mapper_update_hub_score.py,`pwd`/reducer_update_hub_score.py \
  -input hits/input/$((itr-1))/ \
  -output hits/results/$itr/hub \
  -mapper `pwd`/mapper_update_hub_score.py \
  -reducer `pwd`/reducer_update_hub_score.py

  # 2 Обновление авторитетности
  yarn jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -D mapreduce.job.name="HITS Auth Score Update | Job via Streaming" \
  -files `pwd`/mapper_update_auth_score.py,`pwd`/reducer_update_auth_score.py \
  -input hits/results/$itr/hub \
  -output hits/results/$itr/authority \
  -mapper `pwd`/mapper_update_auth_score.py \
  -reducer `pwd`/reducer_update_auth_score.py

  # 3 Подсчёт нормы для посредников
  yarn jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -D mapreduce.job.name="HITS Hub Sum Calculate | Job via Streaming" \
  -files `pwd`/mapper_norm_calculate_hub.py,`pwd`/reducer_norm_calculate_hub.py \
  -input hits/results/$itr/authority \
  -output hits/results/$itr/hub-sum-total \
  -mapper `pwd`/mapper_norm_calculate_hub.py \
  -reducer `pwd`/reducer_norm_calculate_hub.py

  # 4 Нормализация посредников
  yarn jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -D mapreduce.job.name="HITS Hub Normalization | Job via Streaming" \
  -files `pwd`/mapper_normalize_hub.py \
  -input hits/results/$itr/authority \
  -output hits/results/$itr/hub-normalization-result \
  -mapper `pwd`/mapper_normalize_hub.py

  # 5 Подсчёт нормы для авторитетности
  yarn jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -D mapreduce.job.name="HITS Auth Sum Calculate | Job via Streaming" \
  -files `pwd`/mapper_norm_calculate_auth.py,`pwd`/reducer_norm_calculate_auth.py \
  -input hits/results/$itr/hub-normalization-result \
  -output hits/results/$itr/auth-sum-total \
  -mapper `pwd`/mapper_norm_calculate_auth.py \
  -reducer `pwd`/reducer_norm_calculate_auth.py

  # 6 Нормализация авторитетности
  yarn jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -D mapreduce.job.name="HITS Auth Normalization | Job via Streaming" \
  -files `pwd`/mapper_normalize_auth.py \
  -input hits/results/$itr/hub-normalization-result \
  -output hits/input/$itr \
  -mapper `pwd`/mapper_normalize_auth.py
done

hdfs dfs -cat hits/input/$iterations/part-00000
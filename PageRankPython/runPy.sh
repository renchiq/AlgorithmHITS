#!/bin/bash
itr_count=3
for ((itr=1; itr <= $itr_count; itr++)); do
    echo "Doing iteration $itr of $itr_count..."
    hdfs dfs -rm -r PR/itr_$((itr+1))
    yarn jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
        -D mapreduce.job.name="PageRank Job via Streaming" \
        -files $(pwd)/map.py,$(pwd)/reduce.py \
        -input PR/itr_$itr/ \
        -output PR/itr_$((itr+1))/ \
        -mapper $(pwd)/map.py \
        -reducer $(pwd)/reduce.py
done
hdfs dfs -cat PR/itr_$((itr_count+1))/part-00000
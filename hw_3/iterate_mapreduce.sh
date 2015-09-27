#!/bin/bash

if [ "$#" -ne 5 ]; then
    echo "usage: iterate_mapreduce mapper reducer input output iterations"
    exit
fi

mapper=$1
reducer=$2
input=$3
output=$4
iterations=$5

## first iteration
command="\
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
-file $mapper \
-mapper $mapper \
-file $reducer \
-reducer $reducer \
-input $input \
-output $output-0 \
"
echo $command
$command

## the remaing n-1 iterations use the previous output parts as input
for (( i=1; i<$iterations; i++ ))
do
    command="\
    hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
    -file $mapper \
    -mapper $mapper \
    -file $reducer \
    -reducer $reducer \
    -input $output-`expr $i - 1`/part-* \
    -output $output-$i/ \
    "
    echo $command
    $command
done
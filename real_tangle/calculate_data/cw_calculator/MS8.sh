#!/usr/bin/env bash
#source Home/python3/bin/activate
for ((i=1;i<342;i++));
do
  nohup python3 /home/demo/fyg-iota/MS8.py ${i} &
done



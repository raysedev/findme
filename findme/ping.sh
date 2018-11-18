#!/bin/bash
cat log.txt | while read line
do
ping $line
done

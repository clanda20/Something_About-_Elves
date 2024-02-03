#!/bin/bash

OUTPUT=($(python elves.py  tr -d '[],'))
echo ${OUTPUT[0]}
echo ${OUTPUT[1]}
echo ${OUTPUT[2]}
echo ${OUTPUT[3]}

third=${OUTPUT[2]}
echo $third
numbers=$(echo "$third" | tr -cd '[:digit:].')

echo "Number: $numbers"

first_last_digit=${numbers:0:1}${numbers: -1}
echo "the new sum is: $first_last_digit"


#!/bin/bash

OUTPUT=($(python testing.py  tr -d '[],'))
#First 4  lines on the list  
echo ${OUTPUT[0]}  ## getting the size of the array
echo ${OUTPUT[1]}
echo ${OUTPUT[2]}
echo ${OUTPUT[3]}
echo ${OUTPUT[4]}

n=${OUTPUT[0]}
echo "Lines list size in elves.py: $n"

counter=3
final=0

while [ $counter -le $n ]
do 
    third=${OUTPUT[counter]}
    echo "Line Multiple of 3  :$third"
    numbers=$(echo "$third" | tr -cd '[:digit:].')

    echo "Number without characters: $numbers"
    
    first_last_digit=${numbers:0:1}${numbers: -1}
    
    echo "First and last number is: $first_last_digit"
    final=$((first_last_digit+final))
    

    ((counter=counter + 3))
done
echo "The total sum  is : $final"



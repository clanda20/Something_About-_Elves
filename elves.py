#!python  

lines = list()
# read in lines from file
filename = 'resources/read.txt'
with open (filename) as fin:
    for line in fin:
        lines.append(line.strip())
arraySize = len(lines)
print(arraySize)  ## pass to elves.sh file

# Lines array with arrays as elements
print(lines)  # important to keep to pass the array to elves.sh

count = 0
total = 0
while (count < arraySize):
    first_line = lines[count]
    #removing all the non-digit and added it to an array of numbers
    newList0 = [val for val in first_line if val.isdigit()]
    first_digit = int(newList0[0])
    last_digit = int(newList0[-1])
    # converting the elements of the array in a single number.
    number0 = first_digit*10 + last_digit
    count = count + 1
    print("Number by line is: ",number0)
    total += number0
    
print("The total sum is: ",total)



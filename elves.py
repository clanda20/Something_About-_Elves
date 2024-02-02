#!python  
# resources/read.txt"
lines = list()
# read in lines from file
filename = 'resources/read.txt'
with open (filename) as fin:
    for line in fin:
        lines.append(line.strip())

# Lines array with arrays as elements
print(lines)

#First array  Lines[0]  1abc2  
first_line = lines[0]
#removing all the non-digit and added it to an array of numbers
newList0 = [val for val in first_line if val.isdigit()]
first_digit = int(newList0[0])
last_digit = int(newList0[-1])
# converting the elements of the array in a single number.
number0 = first_digit*10 + last_digit
print(number0)

#Second  array Lines[1]  pqr3stu8vwx  
second_line = lines[1]
#removing all the non-digit and added it to an array of numbers
newList1 = [val for val in second_line if val.isdigit()]
first_digit1 = int(newList1[0])
last_digit1 = int(newList1[-1])
# converting the elements of the array in a single number.
number1 = first_digit1*10 + last_digit1
print(number1)

#Thirt array  Lines[2]  a1b2c3d4e5f  
third_line = lines[2]
#removing all the non-digit and added it to an array of numbers
newList2 = [val for val in third_line if val.isdigit()]
first_digit = int(newList2[0])
last_digit = int(newList2[-1])
# converting the elements of the array in a single number.
number2 = first_digit*10 + last_digit
print(number2) 

#Fourth array Lines[3] treb7uchet
fourth_line = lines[3]
#removing all the non-digit and added it to an array of numbers
newList3 = [val for val in fourth_line if val.isdigit()]
first_digit = int(newList3[0])
last_digit = int(newList3[-1])
# converting the elements of the array in a single number.
number3 = first_digit*10 + last_digit
print(number3)

#total sum of all numbers.
sum = number0 + number1 + number2 + number3

print(sum)
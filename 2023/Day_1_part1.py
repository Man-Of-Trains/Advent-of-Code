# Day 1 Part 1 - completed. Can be made more efficient, but it works
file = open('Day1_input.txt', 'r')
data = file.readlines()

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
string_numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero']

total_sum = 0
# Iterate through each of the input lines, take a full string at a time
for i in range(len(data)):
    word = data[i]
    length = len(word)
    number_string = ""
    for char in word:
        if char in numbers:
            number_string += char
    
    if len(number_string) == 1:
        number_string = 2*number_string
    elif len(number_string) == 2:
        number_string = number_string
    elif len(number_string) > 2:
        number_string = number_string[0] + number_string[-1]
    
    total_sum += int(number_string)

print(total_sum)

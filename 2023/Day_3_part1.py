# Day 3 Part 1 - incomplete
file = open('Day3_input.txt', 'r')
data = file.readlines()

for i in range(len(data)):
    data[i] = data[i].replace('\n', '')
    
print(data[0:3])
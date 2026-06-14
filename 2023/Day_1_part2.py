# Day 1 Part 2 - complete. Probably extremely inefficient, but it works. 
data = file.readlines()

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

total_sum = 0
# Iterate through each of the input lines, take a full string at a time
for i in range(len(data)):
    word = data[i]
    idx = 20*[0]
    last_idx = 20*[0]
    for j in range(len(numbers)):
        idx[j] = word.find(numbers[j])
        last_idx[j] = word.rfind(numbers[j])
    total_idx = idx + last_idx

    min_idx = min(n for n in total_idx if n>=0)
    max_idx = max(total_idx)
    
    int_1 = (total_idx.index(min_idx) % 10)
    int_2 = (total_idx.index(max_idx) % 10)
    total_sum += int(str(int_1) + str(int_2))
print(total_sum)
    
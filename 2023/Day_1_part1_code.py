data = open("Day1_input.txt", "r")
data = data.read().split("\n")
data = [str(i) for i in data]
data_int = [[] for _ in range(len(data))]
data_sum = [[] for _ in range(len(data))]
for i in range(len(data)):
    for char in data[i]:
        if char == "1" or char == "2" or char == "3" or char == "4" or char == "5" or char == "6" or char == "7" or char == "8" or char == "9" or char == "0":
            data_int[i].append(int(char))
            continue
        else:
            continue
        
for i in range(len(data)):
    if len(data_int[i]) == 1:
        data_sum[i] = int(str(data_int[i][0]) + str(data_int[i][0]))
    elif len(data_int[i]) == 2:
        data_sum[i] = int(str(data_int[i][0]) + str(data_int[i][1]))
    else:
        data_sum[i] = int(str(data_int[i][0]) + str(data_int[i][-1]))

result = sum(data_sum)
print(result)
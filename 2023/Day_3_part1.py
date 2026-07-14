# Day 3 Part 1 - incomplete
file = open('D:\\Programming\\Github\\Advent-of-Code\\2023\\Input files\\Day3_example.txt', 'r')
data = file.readlines()

for i in range(len(data)):
    data[i] = data[i].replace('\n', '')

print(data[0:3])

ints = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
coords_x = []
coords_y = []
check = []
for i in range(len(data)):
    for j in range(len(data[i])):
        print(f"Row: {i}, Column: {j}, Value: {data[i][j]}")
        if data[i][j] in ints:
            if j == 0 or (j > 0 and data[i][j-1] not in ints):
                coords_x.append(i)
                coords_y.append(j)
                if j != len(data[i])-1 and data[i][j+1] not in ints:
                    check.append(0)
                    continue
                check.append(1)
            if j == len(data[i])-1 or (j < len(data[i])-1 and data[i][j+1] not in ints):
                coords_x.append(i)
                coords_y.append(j)
                if j == 0 or (j > 0 and data[i][j-1] not in ints):
                    check.append(0)
                    continue
                check.append(1)
        
            # print(f"Check: {check}")
            
# sum = 0
# for i in range(len(coords_x)-1):
#     if i > 0:
#         if check[i-1] == 1:
#             continue
#     x = coords_x[i]
#     first_y = coords_y[i]
#     if check[i] == 0:
#         second_y = first_y
#     else:
#         second_y = coords_y[i+1]
#     print(data[x][first_y:second_y+1])
#     number = int(data[x][first_y:second_y+1])
#     print(number)
#     if first_y != 0:
#         y_min = first_y - 1
#     else:
#         y_min = first_y
        
#     if second_y != len(data[x])-1:
#         y_max = second_y + 1
#     else:
#         y_max = second_y
        
#     if x != 0:
#         x_min = x - 1
#     else:
#         x_min = x
    
#     if x != len(data)-1:
#         x_max = x + 1
#     else:
#         x_max = x
        
#     data_x_subset = data[x_min:x_max+1]
#     data_xy_subset = []
#     for k in range(len(data_x_subset)):
#         data_xy_subset.append(data_x_subset[k][y_min:y_max+1])
        
#     if any(char not in ints and char != '.' for row in data_xy_subset for char in row):
#         print(f"Subset: {data_xy_subset}")
#         sum = sum + number
    
# print(sum)
            # if i != 0:
            #     test.append(data[i-1][j])
            #     if j != 0:
            #         test.append(data[i-1][j-1])
            #     if j != len(data[i])-1:
            #         test.append(data[i-1][j+1])
            
            # if i != len(data)-1:
            #     test.append(data[i+1][j])
            #     if j != 0:
            #         test.append(data[i+1][j-1])
            #     if j != len(data[i])-1:
            #         test.append(data[i+1][j+1])
            
            # if j != 0:
            #     test.append(data[i][j-1])
            # if j != len(data[i])-1:
            #     test.append(data[i][j+1])
            # for k in range(len(test)):
            #     if test[k] not in ints and test[k] != '.':
            #         print(f"Valid: {test[k]}")
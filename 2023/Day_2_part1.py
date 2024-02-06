input = open("Day2_input.txt", "r")
data = input.read().split("\n")
delimiters = [":", ";"]
maxRed = 12
maxGreen = 13
maxBlue = 14

game_score = [True for i in range(len(data))]
gameScore = 0
for i in range(len(data)): 
    string = data[i]
    for delimiter in delimiters:
        string = ":".join(string.split(delimiter))
    data[i] = string.split(":")

    for ii in range(len(data[i])):
        data[i][ii] = data[i][ii].split(" ")
        
        red = 0
        green = 0
        blue = 0
        possible = True
        for iii in range(len(data[i][ii])):
            if (data[i][ii][iii] == "red" and int(data[i][ii][iii - 1]) > maxRed):
                possible = False
            elif data[i][ii][iii] == "green" and int(data[i][ii][iii - 1]) > maxGreen:
                possible = False
            elif data[i][ii][iii] == "blue" and int(data[i][ii][iii - 1]) > maxBlue:
                possible = False
            else: 
                continue
        
        if possible == False:
            print(i + 1)
            gameScore += (i + 1)
            break
        
print(5050 - gameScore)
# print(data[3][3][3])
# print(data)

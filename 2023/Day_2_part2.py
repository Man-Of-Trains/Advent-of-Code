# Day 2 Part 2 - complete!
file = open('Day2_input.txt', 'r')
data = file.readlines()

total_sum = 0

for i in range(len(data)):
    game = data[i]
    game = game.replace('\n', '')
    game_split = game.split(": ")
    game_id = game_split[0].split(" ")[1]
    games = game_split[1].split("; ")

    n_red = 0
    n_green = 0
    n_blue = 0

    print(games)
    n_games = len(games)
    
    for j in range(n_games):
        game_j = games[j]
        game_j_split = game_j.split(", ")
        print(game_j_split)
        n_types = len(game_j_split)
        for k in range(n_types):
            game_j_k = game_j_split[k]
            game_j_k_split = game_j_k.split(" ")
            print(game_j_k_split)
            color = game_j_k_split[1]
            n_color = int(game_j_k_split[0])
            
            if color == "red":
                if n_color > n_red:
                    n_red = n_color
            if color == "green":
                if n_color > n_green:
                    n_green = n_color
            if color == "blue":
                if n_color > n_blue:
                    n_blue = n_color
    
    power = n_red * n_green * n_blue
    total_sum += power
    
    print("--------------------")

print("Total sum of valid game IDs: " + str(total_sum))
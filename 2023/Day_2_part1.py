# Day 2 Part 1 - complete!
file = open('Day2_input.txt', 'r')
data = file.readlines()

n_red = 12
n_green = 13
n_blue = 14

total_sum = 0

for i in range(len(data)):
    game = data[i]
    game = game.replace('\n', '')
    game_split = game.split(": ")
    game_id = game_split[0].split(" ")[1]
    games = game_split[1].split("; ")

    print(games)
    n_games = len(games)
    
    game_valid = True
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
                    game_valid = False
                    break
            if color == "green":
                if n_color > n_green:
                    game_valid = False
                    break
            if color == "blue":
                if n_color > n_blue:
                    game_valid = False
                    break
    
    if game_valid:
        print("Game " + game_id + " is valid")
        total_sum += int(game_id)
    
    print("--------------------")

print("Total sum of valid game IDs: " + str(total_sum))
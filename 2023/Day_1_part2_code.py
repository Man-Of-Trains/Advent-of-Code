# import re

# data = open("Day1_input.txt", "r")
# data = data.read().split("\n")
# data = [str(i) for i in data]
# data_int = [[] for _ in range(len(data))]
# data_sum = [[] for _ in range(len(data))]

# def extract_integers(input_string):
#     # Define a regular expression pattern to match integers and integer words
#     pattern = re.compile(r'(?:zero|one|two|three|four|five|six|seven|eight|nine|\d)')
    
#     # Use findall to extract all matches from the input string
#     matches = pattern.findall(input_string)
    
#     # Convert integer words to corresponding numerical values
#     result = [int(match) if match.isdigit() else ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'].index(match) for match in matches]
    
#     return result

# for i in range(len(data)):
#     data_int[i] = extract_integers(data[i])
        
# for i in range(len(data)):
#     if len(data_int[i]) == 1:
#         data_sum[i] = int(str(data_int[i][0]) + str(data_int[i][0]))
#     elif len(data_int[i]) == 2:
#         data_sum[i] = int(str(data_int[i][0]) + str(data_int[i][1]))
#     else:
#         data_sum[i] = int(str(data_int[i][0]) + str(data_int[i][-1]))

# result = sum(data_sum)
# print(result)

def make_trie (word_array):
    trie = {}
    current = None

    for i in range(len(word_array)):
        current = trie
        for c in word_array[i]:
            if c not in current: 
                current[c] = {}
            current = current[c]

        current["value"] = i + 1


    return trie

def parse_line(line):
    
    english_numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    root = make_trie(english_numbers)

    result = ""
    current_node = root
    last_char = ''


    for c in line:

        # Literal number
        if c.isnumeric():
            result += c
            current_node = root
            continue

        print("Char {} --> ".format(c))
        if c in current_node:
            # current char is the follow up to the last character
            current_node = current_node[c]
        else:
            # last char is not follow up
            if last_char in root and c in root[last_char]:
                # ... but last char is a starting char and current char is a follow up
                # eightwo case
                current_node = root[last_char][c]

            elif c in root:
                # ... current char is not a follow up to anything but is a starting char
                current_node = root[c]


        if 'value' in current_node:
            result += repr(current_node['value'])


        last_char = c
        



    return result

def get_calibration(line):
    numbers = parse_line(line)
    if len(numbers) == 1:
        num = int(numbers[0] + numbers[0])
    else:
        num = int(numbers[0] + numbers[-1])
    return num

def main():
    total = 0

    with open("Day1_input.txt", 'r') as inf:
        for line in inf:
            total += get_calibration(line)

    print(total)

if __name__ == "__main__":
    main()
def part_one():
    line_count = 0
    lines = []
    values = None

    with open("Day3PuzzleInput.txt") as files:
        lines = files.readlines()

    length = len(lines[0]) - 1
    values = [0] * length

    for line in lines:
        for index in range(length):
            values[index] += int(line[index])

    epsilon_rate = ''
    gamma_rate = ''

    for value in values:
        if (value > (len(lines) / 2)):
            gamma_rate += "1"
            epsilon_rate += "0"
        else:
            gamma_rate += "0"
            epsilon_rate += "1"

    print(int(gamma_rate, 2) * (int(epsilon_rate, 2)))

def part_two():
    current_index = 0
    line_count = 0
    lines = []

    with open("Day3PuzzleInput.txt") as files:
        lines = files.readlines()

    length = len(lines[0]) - 1

    while(len(lines) > 1):
        most_common_bit = get_most_common_bit(lines, current_index)
        lines = filter_strings(lines, current_index, most_common_bit)
        current_index += 1

    oxygen_generator_rating = (lines[0])

    with open("Day3PuzzleInput.txt") as files:
        lines = files.readlines()

    current_index = 0

    while(len(lines) > 1):
        least_common_bit = get_least_common_bit(lines, current_index)
        lines = filter_strings(lines, current_index, least_common_bit)
        current_index += 1

    c02_scrubber_rating = (lines[0])
    print(int(c02_scrubber_rating, 2) * (int(oxygen_generator_rating, 2)))


def get_most_common_bit(strings, index):
    bit_count = 0

    for string in strings:
        bit_count += int(string[index])

    if(bit_count < (len(strings) / 2)):
        return "0"
    else:
        return "1"

def get_least_common_bit(strings, index):
    bit_count = int(0)

    for string in strings:
        bit_count += int(string[index])

    if(bit_count < (len(strings) / 2)):
        return "1"
    else:        
        return "0"

def filter_strings(strings, index, char):
    return_strings = []

    for string in strings:
        if(string[index] == char):
            return_strings.append(string)

    return return_strings

def invert_string(string):
    return_string = ""

    for char in string:
        if(char == "1"):
            return_string += "0"
        else:
            return_string += "1"

    return return_string

part_one()
part_two()

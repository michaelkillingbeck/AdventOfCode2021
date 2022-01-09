import math

file_name = "Day14PuzzleInput.txt"

def calculate_difference_between_highest_and_lowest(source_dictionary):
    chars_dictionary = {}

    for (key, value) in source_dictionary.items():
        for char in key:
            #print("Char: %s" % char)
            if char not in chars_dictionary:
                chars_dictionary[char] = value
            else:
                chars_dictionary[char] += value

    letters_count = {}

    for (key, value) in chars_dictionary.items():
        letters_count[key] = math.ceil(value / 2)

    maximum = minimum = None

    for (char, value) in letters_count.items():
        if(maximum is None or value > maximum):
            maximum = value
        if(minimum is None or value < minimum):
            minimum = value

    print("Maximum: %s, Minimum %s, Difference %s" % (maximum, minimum, (maximum - minimum)))

def create_initial_pairs(source):
    pairs = []

    for index in range(len(source.strip()) - 1):
        pairs.append(source[index] + source[index + 1])

    return pairs

def create_rules_dictionary(lines):
    rules_dictionary = {}

    for line in lines:
        sections = line.split()
        rules_dictionary[sections[0]] = { sections[0][0] + sections[2], sections[2] + sections[0][1] }

    print(rules_dictionary)

    return rules_dictionary

def get_insertion_rules(lines):
    rules = []

    for line in lines:
        if "->" in line:
            rules.append(line)

    return rules

def get_puzzle_input(filename):
    lines = []

    with open(filename) as file:
        lines = file.readlines()

    return lines

def perform_steps(steps, template, rules):
    current_step = 1
    pairs_count = {}

    for rule in rules:
        pairs_count[rule] = 0

    pairs = create_initial_pairs(template)

    for pair in pairs:
        first, second = rules[pair]
        pairs_count[first] += 1
        pairs_count[second] += 1

    while current_step < steps:
        temp_count = {}
        for pair in pairs_count:
            temp_count[pair] = 0

        for (pair, count) in pairs_count.items():
            #print("Pair: %s Count: %s" % (pair, count))
            (first, second) = rules[pair]
            temp_count[first] += count
            temp_count[second] += count

        pairs_count = temp_count
        current_step += 1

        local_count = 0
        for pair, count in pairs_count.items():
            #print("Pair: %s Count: %s" % (pair, count))
            local_count += count

        print("Length of string after step %s is %s" % (current_step, local_count + 1))

    return pairs_count

puzzle_input = get_puzzle_input(file_name)
rules = get_insertion_rules(puzzle_input)
rules_dictionary = create_rules_dictionary(rules)
initial_template = puzzle_input[0].strip()
pairs_dictionary = perform_steps(10, initial_template, rules_dictionary)
calculate_difference_between_highest_and_lowest(pairs_dictionary)
pairs_dictionary = perform_steps(40, initial_template, rules_dictionary)
calculate_difference_between_highest_and_lowest(pairs_dictionary)

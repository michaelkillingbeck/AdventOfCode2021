def calculate_output(line, mappings):
    answer_string = ""
    numbers = line.split()

    for index in range(len(numbers)):
        numbers[index] = "".join(sorted(numbers[index]))

    for number in numbers:
        for index in range(len(mappings)):
            if(mappings[index] == number):
                answer_string += str(index)
                break

    return int(answer_string)


def create_mappings(line):
    input_data = line.strip().split('|')[0].strip().split()

    for index in range(len(input_data)):
        input_data[index] = "".join(sorted(input_data[index]))

    mapping_data = [""] * 10

    mapping_data[1] = list(filter(lambda entry: len(entry) == 2, input_data))[0] 
    mapping_data[4] = list(filter(lambda entry: len(entry) == 4, input_data))[0]
    mapping_data[7] = list(filter(lambda entry: len(entry) == 3, input_data))[0]
    mapping_data[8] = list(filter(lambda entry: len(entry) == 7, input_data))[0]
    mapping_data[3] = list(filter(lambda entry: len(entry) == 5 and includes(entry, mapping_data[1]), input_data))[0]
    mapping_data[9] = list(filter(lambda entry: len(entry) == 6 and includes(entry, mapping_data[3]), input_data))[0]
    mapping_data[6] = list(filter(lambda entry: len(entry) == 6 and includes(entry, mapping_data[9]) == False and includes(entry, mapping_data[1]) == False, input_data))[0]
    mapping_data[0] = list(filter(lambda entry: len(entry) == 6 and includes(entry, mapping_data[9]) == False and includes(entry, mapping_data[6]) == False, input_data))[0]
    mapping_data[2] = list(filter(lambda entry: len(entry) == 5 and includes(entry, mapping_data[3]) == False and includes((entry + mapping_data[6]), mapping_data[8]), input_data))[0]

    for entry in input_data:
        found = False
        for index in range(len(mapping_data)):
            if(mapping_data[index] == entry):
                found = True
                break
        if(found == False):
            mapping_data[5] = entry

    return mapping_data

def get_input(filename, output_only):
    results = []

    with open(filename) as file:
        lines = file.readlines()

    for line in lines:
        input_line = line.split('|')
        if(len(input_line) > 1):
            if(output_only):
                results.append(input_line[1].strip())
            else:
                results.append(line.strip())

    return results

def includes(data_to_test, input_data):
    #print("Testing %s with %s" % (data_to_test, input_data))
    input_chars = input_data.split()

    for char in input_data:
        if char not in data_to_test:
            return False

    return True

def part_one(input_array):
    part_one_answer = 0

    for entry in input_array:
        output_numbers = entry.split()

        for number in output_numbers:
            length = len(number)

            if(length == 2
                    or length == 3
                    or length == 4
                    or length ==7):
                part_one_answer += 1

    print("Part one answer is %s" % part_one_answer)

def part_two(input_array):
    part_two_answer = 0

    for line in input_array:
        mappings = create_mappings(line)
        output = line.split('|')[1].strip()
        part_two_answer += calculate_output(output, mappings) 

    print("Part two answer is %s" %part_two_answer)

results = get_input("Day8PuzzleInput.txt", True)
part_one(results)
results = get_input("Day8PuzzleInput.txt", False)
part_two(results)


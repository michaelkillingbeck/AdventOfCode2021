def create_values_array(input_array):
    max_value = max(input_array)
    min_value = min(input_array)
    values_array = [0] * (max_value + 1)

    for value in input_array:
        values_array[value] += 1

    return values_array

def get_input(filename):
    lines = []
    results = []
    with open(filename) as file:
        lines =  file.readlines()

    for line in lines:
        for number in line.rstrip().split(','):
            if(len(number) > 0):
                results.append(int(number))

    return results

def part_one(values):
    local_minimum = None
    new_answer = None

    for target in range(len(values) + 1):
        current_amount = 0
        for value in range(len(values)):
            fuel_needed = abs(target - value) * values[value]
            current_amount += fuel_needed

            if(local_minimum != None and local_minimum < current_amount):
                break
            
        if(local_minimum is None or current_amount < local_minimum):
            local_minimum = current_amount
            new_answer = target

    print("Answer is %s and Fuel Needed is %s" % (new_answer, local_minimum))

def part_two(values):
    local_minimum = None
    new_answer = None

    for target in range(len(values) + 1):
        current_amount = 0
        for value in range(len(values)):
            fuel_needed = 0
            steps_needed = abs(target - value)
            
            for step in range(steps_needed + 1):
                fuel_needed += step

            fuel_needed *= values[value]
            current_amount += fuel_needed

            if(local_minimum != None and local_minimum < current_amount):
                break
    
        if(local_minimum is None or current_amount < local_minimum):
            local_minimum = current_amount
            new_answer = target

    print("Answer is %s and Fuel Needed is %s" % (new_answer, local_minimum))

input_array = get_input("Day7PuzzleInput.txt")
values = create_values_array(input_array)

part_one(values)
part_two(values)

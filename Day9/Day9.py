import time

def calculate_basin(data, row, column, current_size, check_up, check_down, check_left, check_right, checked_coords):
    current_coord = ("%s,%s" % (row, column))
    checked_coords.append(current_coord)
    
    if(check_up and row > 0 and int(data[row - 1][column]) < 9):
        next_coord = ("%s,%s" % (row - 1, column))
        if(next_coord not in checked_coords):
            current_size = calculate_basin(data, row - 1, column, current_size + 1, True, False, True, True, checked_coords)

    if(check_down and row < len(data) - 1 and int(data[row + 1][column]) < 9):
        next_coord = ("%s,%s" % (row + 1, column))
        if(next_coord not in checked_coords):
            current_size = calculate_basin(data, row + 1, column, current_size + 1, False, True, True, True, checked_coords)

    if(check_left and column > 0 and int(data[row][column - 1]) < 9):
        next_coord = ("%s,%s" % (row, column - 1))
        if(next_coord not in checked_coords):
            current_size = calculate_basin(data, row, column - 1, current_size + 1, True, True, True, False, checked_coords)

    if(check_right and column < len(data[row]) - 1 and int(data[row][column + 1]) < 9):
        next_coord = ("%s,%s" % (row, column + 1))
        if(next_coord not in checked_coords):
            current_size = calculate_basin(data, row, column + 1, current_size + 1, True, True, False, True, checked_coords)

    return current_size

def calculate_part_one(puzzle_input):
    low_points = []

    rows = len(puzzle_input)
    columns = len(puzzle_input[0])

    for row in range(rows):
        for column in range(columns):
            lower_than = 0
            cell = puzzle_input[row][column]
            
            #check below
            if(row == rows - 1 or puzzle_input[row + 1][column] > cell):
                lower_than += 1
            #check above
            if(row == 0 or puzzle_input[row - 1][column] > cell):
                lower_than += 1
            #check left
            if(column == 0 or puzzle_input[row][column - 1] > cell):
                lower_than += 1
            #check right
            if(column == columns - 1 or puzzle_input[row][column + 1] > cell):
                lower_than += 1

            if(lower_than == 4):
                low_points.append(int(cell))

    return low_points

def calculate_part_two(puzzle_input):
    basins = []
    columns = len(puzzle_input[0])
    rows = len(puzzle_input)

    for row in range(rows):
        for column in range(columns):
            lower_than = 0
            cell = puzzle_input[row][column]
            
            #check below
            if(row == rows - 1 or puzzle_input[row + 1][column] > cell):
                lower_than += 1
            #check above
            if(row == 0 or puzzle_input[row - 1][column] > cell):
                lower_than += 1
            #check left
            if(column == 0 or puzzle_input[row][column - 1] > cell):
                lower_than += 1
            #check right
            if(column == columns - 1 or puzzle_input[row][column + 1] > cell):
                lower_than += 1

            if(lower_than == 4):
                basin_size = calculate_basin(puzzle_input, row, column, 1, True, True, True, True, [])
                print("Basin found at %s,%s and the size is %s" % (row, column, basin_size))
                basins.append(int(basin_size))

    sorted_basins = sorted(basins, reverse = True)
    print(sorted_basins)
    part_two_answer = sorted_basins[0] * sorted_basins[1] * sorted_basins[2]
    print("Part two answer is %s" % part_two_answer)

def get_puzzle_input(filename):
    lines = []
    with open(filename) as file:
        lines = file.readlines()
    
    results = []
    for line in lines:
        if(len(line) > 1):
            temp_line = []
            for char in line.strip():
                temp_line.append(char)

            results.append(temp_line)

    return results

puzzle_input = get_puzzle_input("Day9PuzzleInput.txt")
results = calculate_part_one(puzzle_input)
print(results)
print("Answer to Part One is %s" % (sum(results) + len(results)))
calculate_part_two(puzzle_input)

class GridCell:
    has_flashed = False
    value = 0

    def __init__(self, starting_value):
        self.value = starting_value

    def get_flashed_status(self):
        if(self.has_flashed):
            return 1
        else:
            return 0

    def increment(self):
        if(self.has_flashed == False):
            self.value += 1

    def reset(self):
        self.has_flashed = False
        if(self.value > 9):
            self.value = 0

    def set_flash(self):
        self.has_flashed = True

    def should_flash(self):
        return self.value > 9 and self.has_flashed == False

def get_flashes(grid):
    local_count = 0

    for row in range(len(grid)):
        for column in range(len(grid[row])):
            local_count += grid[row][column].get_flashed_status()

    return local_count

def get_grid(filename):
    lines = []

    with open(filename) as file:
        lines = file.readlines()

    grid = []
    for line in lines:
        temp_line = list(line.strip())
        temp_list = []

        if(len(temp_line) > 0):
            for item in temp_line:
                temp_list.append(GridCell(int(item)))
            grid.append(temp_list)

    return grid

def grid_synchronized(grid):
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if(grid[row][column].get_flashed_status() == 0):
                return False

    return True

def needs_to_flash(grid):
    for row in grid:
        for cell in row:
            if(cell.should_flash()):
                return True

    return False

def part_one(grid, steps):
    current_step = 1
    answer = 0

    while current_step <= steps:
        for row in range(len(grid)):
            for column in range(len(grid[row])):
                grid[row][column].increment()
            
        while(needs_to_flash(grid)):
            for row in range(len(grid)):
                for column in range(len(grid[row])):
                    if(grid[row][column].should_flash()):
                        grid[row][column].set_flash()
                        grid = update_neighbours(grid, row, column)

        answer += get_flashes(grid)
        reset_grid(grid)
        current_step += 1

    print("Part one answer is %s" % answer)

def part_two(grid):
    all_flashed = False
    current_step = 0

    while all_flashed == False:
        current_step += 1
        for row in range(len(grid)):
            for column in range(len(grid[row])):
                grid[row][column].increment()
            
        while(needs_to_flash(grid)):
            for row in range(len(grid)):
                for column in range(len(grid[row])):
                    if(grid[row][column].should_flash()):
                        grid[row][column].set_flash()
                        grid = update_neighbours(grid, row, column)

        print("Step %s:" %current_step)
        all_flashed = grid_synchronized(grid)
        reset_grid(grid)
        print_grid(grid)

    print("Part two answer is %s" % current_step)

def print_grid(grid):
    for line in grid:
        values = []
        for cell in line:
            values.append(cell.value)
        print(values)

def reset_grid(grid):
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            grid[row][column].reset()

def update_neighbours(grid, row, column):
    if(row > 0):
        grid[row - 1][column].increment()
        if(column > 0):
            grid[row - 1][column - 1].increment()
        if(column < len(grid[row]) - 1):
            grid[row - 1][column + 1].increment()

    if(column > 0):
        grid[row][column - 1].increment()
    if(column < len(grid[row]) - 1):
        grid[row][column + 1].increment()

    if(row < len(grid) - 1):
        grid[row + 1][column].increment()
        if(column > 0):
            grid[row + 1][column - 1].increment()
        if(column < len(grid[row]) - 1):
            grid[row + 1][column + 1].increment()

    return grid

grid = get_grid("Day11PuzzleInput.txt")
print_grid(grid)
part_one(grid, 100)
part_two(grid)

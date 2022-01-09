input_file = "Day13PuzzleInput.txt"

class Fold:
    direction = ""
    value = 0

    def __init__(self, instruction):
        sections = instruction.split('=')

        self.direction = sections[0]
        self.value = int(sections[1])

    def to_string(self):
        return str("Direction %s, Value %s" % (self.direction, self.value))

class Point:
    x = 0
    y = 0

    def __init__(self, input_line):
        coords = input_line.split(',')

        self.x = int(coords[0])
        self.y = int(coords[1])

    def to_string(self):
        return str("%s , %s" % (self.x, self.y))

def count_dots(page):
    count = 0

    for row in range(len(page)):
        for column in range(len(page[0])):
            if(page[row][column] == '#'):
                count += 1

    return count

def create_dots_array(x, y, dots):
    page = [['.' for column in range(x + 1)] for row in range(y + 1)]

    for dot in dots:
        page[dot.y][dot.x] = '#'

    return page

def fold_left(fold_value, page):
    folded_page = [['.' for column in range(fold_value)] for row in range(len(page))]
    
    for row in range(len(page)):
        for column in range(len(folded_page[row])):
            folded_page[row][column] = page[row][column]

    current_column = 0

    while(current_column < fold_value):
        source_index = (fold_value * 2) - current_column

        for row in range(len(folded_page)):
            if(source_index < len(page[row])):
                if(page[row][source_index] == '#'):
                    folded_page[row][current_column] = '#'

        current_column += 1

    return folded_page


def fold_up(fold_value, page):
    folded_page = [['.' for column in range(len(page[0]))] for row in range(fold_value)]
   
    for row in range(len(folded_page)):
        for column in range(len(folded_page[row])):
            folded_page[row][column] = page[row][column]

    for index in range(fold_value):
        source_index = (fold_value * 2) - index

        if(source_index < len(page)):
            source_row = page[source_index]

            for cell in range(len(source_row)):
                if(source_row[cell] == '#'):
                    folded_page[index][cell] = '#'

    return folded_page

def get_dots_layout(filename):
    lines = []

    with open(filename) as file:
        lines = file.readlines()

    dots_input = []

    for line in lines:
        if(line[0].isnumeric()):
            dots_input.append(Point(line.strip()))

    return dots_input

def get_folds(filename):
    lines = []

    with open(filename) as file:
        lines = file.readlines()

    folds = []

    for line in lines:
        if(len(line) > 0):
            words = line.split()
            if(len(words) > 0 and words[0] == "fold"):
                folds.append(Fold(words[2]))

    return folds   

def get_maximum_x(dots):
    local_max = 0

    for dot in dots:
        if(dot.x > local_max):
            local_max = dot.x

    return local_max

def get_maximum_y(dots):
    local_max = 0

    for dot in dots:
        if(dot.y > local_max):
            local_max = dot.y

    return local_max

def perform_folds(folds, page):
    folded_page = page

    for fold in folds:
        #print(fold.to_string())
        if(fold.direction == 'y'):
            folded_page = fold_up(fold.value, folded_page)
        elif(fold.direction == 'x'):
            folded_page = fold_left(fold.value, folded_page)

        #for line in folded_page:
            #print(line)
        visible_dots = count_dots(folded_page)
        print("There are %s visible dots" %visible_dots)

    for line in folded_page:
        print("".join(line))

dots = get_dots_layout(input_file)
max_x = get_maximum_x(dots)
max_y = get_maximum_y(dots)
dots_array = create_dots_array(max_x, max_y, dots)
fold_instructions = get_folds(input_file)
perform_folds(fold_instructions, dots_array)

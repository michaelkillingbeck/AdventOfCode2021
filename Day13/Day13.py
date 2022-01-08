input_file = "SmallSample.txt"

class Fold:
    direction = ""
    value = 0

    def __init__(self, instruction):
        sections = instruction.split('=')

        direction = sections[0]
        value = sections[1]

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

def create_dots_array(x, y, dots):
    page = [['.' for column in range(x + 1)] for row in range(y + 1)]

    for dot in dots:
        page[dot.y][dot.x] = '#'

    return page

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

dots = get_dots_layout(input_file)
max_x = get_maximum_x(dots)
max_y = get_maximum_y(dots)
dots_array = create_dots_array(max_x, max_y, dots)
fold_instructions = get_folds(input_file)

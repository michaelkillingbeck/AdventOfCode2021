class Path:
    start = ""
    end = ""

    def __init__(self, line_string):
        sections = line_string.split('-')
        self.start = sections[0].strip()
        self.end = sections[1].strip()

    def is_end(self):
        return self.end == "end"

    def is_start(self):
        return self.start == "start"

    def to_string(self):
        return "%s->%s" % (self.start, self.end)

def create_paths(lines):
    paths = []

    for line in lines:
        paths.append(Path(line))

    return paths

def get_input(filename):
    lines = []

    with open(filename) as file:
        lines = file.readlines()

    return lines

def part_one(paths):
    answers = []

    starting_points = filter(lambda path: path.is_start(), paths)
    all_paths = []

    for point in starting_points:
        traverse_paths(all_paths, [], point, paths)
        print(all_paths)

def print_paths(paths):
    for path in paths:
        print(path.to_string())

def traverse_paths(all_paths, current_path, point, paths):
    current_path.append(point.start)
    
    next_points = []
    for path in paths:
        if(path.start == point.end):
            next_points.append(path)

    if(len(next_points) > 0):
        for next_point in next_points:
            print("Next point: %s" %next_point.to_string())
            all_paths.append(traverse_paths(all_paths, current_path, next_point, paths))
    
    current_path.append(point.end)
    print("Final path: %s" %current_path)
    return current_path

puzzle_input = get_input("SmallSample.txt")
paths = create_paths(puzzle_input)
part_one(paths)

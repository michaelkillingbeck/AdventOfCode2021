import time
small_caves_only_once = True
#sleep_time = 0.75

class Path:
    start = ""
    end = ""

    def __init__(self, line_string):
        #print(line_string)
        sections = line_string.split('-')
        self.start = sections[0].strip()
        self.end = sections[1].strip()

    def is_end(self):
        return self.end == "end" or self.start == "end"

    def is_start(self):
        return self.start == "start" or self.end == "start"

    def reverse(self):
        return Path("%s-%s" %(self.end, self.start))

    def to_string(self):
        return "%s->%s" % (self.start, self.end)

def can_be_visited(end_point, total_route):
    if(end_point.isupper()):
        return True

    if(end_point == "start"):
        return False

    for char in total_route:
        if(end_point == char):
            if(can_visit_again(char, total_route) == False):
                return False

    return True

def can_visit_again(char, total_route):
    if(small_caves_only_once):
        return False

    visited_places = []

    for place in total_route:
        if place.islower():
            #print("Place is %s" %place)

            for visited_place in visited_places:
                if visited_place == place:
                    return False

            visited_places.append(place)
    
    #print("Can visit %s again" %char)
    #print("Total route is: %s" %total_route)
    return True

def create_paths(lines):
    paths = []

    for line in lines:
        if(len(line) > 1):
            paths.append(Path(line))

    return paths

def get_input(filename):
    lines = []

    with open(filename) as file:
        lines = file.readlines()

    return lines

def calculate_paths(paths):
    answers = []

    starting_points = filter(lambda path: path.is_start(), paths)
    all_paths = []

    for point in starting_points:
        start = None
        if(point.end == "start"):
            start = point.reverse()
        else:
            start = point

        traverse_paths(all_paths, [start.start], start.end, paths)

    finished_paths = []
    for path in all_paths:
        end_node = path[-1]
        if(end_node == "end"):
            finished_paths.append(path)

    #print("Final paths:")
    #for path in finished_paths:
        #print(path)

    print("Total paths found: %s" %len(finished_paths))

def print_paths(paths):
    for path in paths:
        print(path.to_string())

def traverse_paths(all_paths, current_path, point, paths):
    current_path.append(point)
    #print("Current path is %s" %current_path)
    #time.sleep(sleep_time)

    next_points = []
    #print("Looking for routes from %s" %point)
    for path in paths:
        if(path.start == point and can_be_visited(path.end, current_path)):
            next_points.append(path)
        elif(path.end == point and can_be_visited(path.start, current_path)):
            next_points.append(path.reverse())
    
    #time.sleep(sleep_time)

    if(len(next_points) > 0 and point != "end"):
        for next_point in next_points:
            #print("Next point: %s" %next_point.to_string())
            #time.sleep(sleep_time)
            temp_current_path = current_path[:]
            all_paths.append(traverse_paths(all_paths, temp_current_path, next_point.end, paths))
    
    #print("Final path: %s" %current_path)
    return current_path

puzzle_input = get_input("Day12PuzzleInput.txt")
paths = create_paths(puzzle_input)
calculate_paths(paths)
small_caves_only_once = False
calculate_paths(paths)

class Point:
    def __init__(self, coordinates_array):
        self.x = int(coordinates_array[0])
        self.y = int(coordinates_array[1])

    def add(self, other):
        self.x += other.x
        self.y += other.y

    def equals(self, other):
        return self.x == other.x and self.y == other.y

    def get_movement_vector(self, other):
        if(self.y == other.y):
            if(self.x < other.x):
                return Point([1, 0])
            elif(self.x > other.x):
                return Point([-1, 0])

        if(self.x == other.x):
            if(self.y < other.y):
                return Point([0, 1])
            elif(self.y > other.y):
                return Point([0, -1])

        movement_x = 0
        movement_y = 0

        if(self.x > other.x):
            movement_x = -1
        elif(self.x < other.x):
            movement_x = 1

        if(self.y > other.y):
            movement_y = -1
        elif(self.y < other.y):
            movement_y = 1

        return Point([movement_x, movement_y])

    def is_diagonal_to(self, other):
        if(self.x == other.x or self.y == other.y):
            return False

        if(abs(self.x - other.x) != abs(self.y - other.y)):
            return False

        return True

    def is_level_with(self, other):
        if(self.x == other.x or self.y == other.y):
            return True

        return False

    def move_to(self, other):
        movement_points = []
        movement_point = self.get_movement_vector(other)

        while(self.equals(other) == False):
            movement_points.append(Point([self.x, self.y]))
            self.add(movement_point)

        movement_points.append(Point([self.x, self.y]))

        return movement_points

    def print(self):
        print("%s , %s" % (self.x, self.y))

def part_one():
    lines = read_input_from_file("Day5PuzzleInput.txt")
    maximum = calculate_maximum(lines)
    points = []

    matrix = [[0 for x in range(maximum)] for y in range(maximum)]
    points = create_points(points, lines)

    while len(points) > 1:
        point1 = points.pop(0)
        point2 = points.pop(0)

        if(point1.is_level_with(point2)):
            points_to_move = point1.move_to(point2)

            for point in points_to_move:
                matrix[point.x][point.y] += 1

    count = 0

    for row in matrix:
        for cell in row:
            if cell > 1:
                count += 1
    
    print(count)

def part_two():
    lines = read_input_from_file("Day5PuzzleInput.txt")
    maximum = calculate_maximum(lines)
    points = []

    matrix = [[0 for x in range(maximum)] for y in range(maximum)]
    points = create_points(points, lines)

    while len(points) > 1:
        point1 = points.pop(0)
        point2 = points.pop(0)

        if(point1.is_level_with(point2)):
            points_to_move = point1.move_to(point2)

        if(point1.is_diagonal_to(point2)):
            points_to_move = point1.move_to(point2)

        for point in points_to_move:
            matrix[point.x][point.y] += 1

    count = 0

    for row in matrix:
        for cell in row:
            if cell > 1:
                count += 1

    print(count)

def calculate_maximum(lines):
    local_maximum = 0

    for line in lines:
        line = line.rstrip()

        if(len(line) > 0):
            segments = line.rstrip().split("->")
            for segment in segments:
                coordinates = segment.split(",")
                for coordinate in coordinates:
                    local_coordinate = int(coordinate)
                    if(local_coordinate > local_maximum):
                        local_maximum = local_coordinate

    return local_maximum + 1

def create_points(points, lines):
    for line in lines:
        line = line.rstrip()

        if(len(line) > 0):
            segments = line.rstrip().split("->")
            for segment in segments:
                coordinates = segment.split(",")
                points.append(Point(coordinates))

    return points

def read_input_from_file(path):
    with open(path) as file:
        return file.readlines()

part_one()
part_two()

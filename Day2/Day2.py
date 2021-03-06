def part_one():
    horizontal = 0
    lines = []
    vertical = 0

    with open("Day2PuzzleInput.txt") as file:
        lines = file.readlines()

    for line in lines:
        command = line.split()

        if (len(command) > 1):
            distance = int(command[1])
            direction = command[0]

            if (direction == 'forward'):
                horizontal += distance
            elif (direction == 'down'):
                vertical += distance
            elif (direction == 'up'):
                vertical -= distance

    print(vertical * horizontal)

def part_two():
    aim = 0
    horizontal = 0
    lines = []
    vertical = 0

    with open("Day2PuzzleInput.txt") as file:
        lines = file.readlines()

    for line in lines:
        command = line.split()
        
        if(len(command) > 1):
            distance = int(command[1])
            direction = command[0]

            if (direction == 'down'):
                aim += distance
            elif (direction == 'up'):
                aim -= distance
            elif (direction == 'forward'):
                horizontal += distance
                vertical += (distance * aim)

    print (vertical * horizontal)

part_one()
part_two()

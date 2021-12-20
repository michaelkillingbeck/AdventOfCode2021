def part_one():
    count =  0
    lastLine = 0
    lines = []
    part1Answer = 0

    with open('Day1Puzzle1Input.txt') as file:
        lines = file.readlines()

    for line in lines:
        count += 1
        newLine = int(line)

        if (newLine > lastLine & lastLine != 0):
            part1Answer += 1

        lastLine = newLine

    print (part1Answer)

def part_two():
    count = 0
    currentSum = 0
    lastSum = 0
    lines = []
    part2Answer = 0
    queue = []
    
    with open('Day1Puzzle1Input.txt') as file:
        lines = file.readlines()

    for line in lines:
        count += 1

        if(count > 3):
            queue.pop(0)

        queue.append(int(line))

        if (count >= 3):
            currentSum = queue[0] + queue[1] + queue[2]
    
        if (currentSum > lastSum & lastSum != 0):
            part2Answer += 1

        lastSum = currentSum

    print(part2Answer)

part_one()
part_two()

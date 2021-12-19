lines = []
lastLine = 0
count = 0
part1Answer = 0
sum = 0
lastSum = 0

with open('Day1Puzzle1Input.txt') as file:
    lines = file.readlines()

for line in lines:
    count += 1
    newLine = int(line)

    if (newLine > lastLine & lastLine != 0):
        part1Answer += 1

    lastLine = newLine

print (part1Answer)
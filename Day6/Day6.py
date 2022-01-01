def part_one_and_two(days_to_simulate):
    current_day = 0
    fish_by_day = [0] * 9
    lantern_fish = get_input("Day6PuzzleInput.txt")
    
    for fish in lantern_fish:
        fish_by_day[fish] += 1

    while(current_day < days_to_simulate):
        fish_by_day = increment_fish_life_cycle(fish_by_day)
        fish_by_day[6] += fish_by_day[8]
        current_day += 1

    print("Number of Fish: %s" % sum(fish_by_day))

def get_input(file_name):
    with open(file_name) as file:
        lines = file.readlines()

    fish = []

    for line in lines:
        fish_line = line.split(',')
        for number in fish_line:
            fish.append(int(number))

    return fish

def increment_fish_life_cycle(fishes):
    first_fish = fishes.pop(0)
    fishes.append(first_fish)

    return fishes

part_one_and_two(256)

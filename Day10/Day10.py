def complete_line(opened_chars):
    results = []

    for char in opened_chars:
        if(char == '('):
            results.append(')')
        elif(char == '['):
            results.append(']')
        elif(char == '{'):
            results.append('}')
        elif(char == '<'):
            results.append('>')
        else:
            print("Unexpected char received (%s)" % char)

    return results

def part_one(lines):
    closing_chars = ")]}>"
    opening_chars = "([{<"

    corrupted_lines = []
    illegal_chars = []

    for line in lines:
        opened_chars = []
        for char in line:
            if(char in opening_chars):
                opened_chars.append(char)
            elif(char in closing_chars):
                char_to_close = opened_chars.pop()
                if(illegally_closed(char_to_close, char)):
                    corrupted_lines.append(line)
                    illegal_chars.append(char)
                    break

    answer = 0

    for char in illegal_chars:
        if(char == ')'):
            answer += 3
        elif(char == ']'):
            answer += 57
        elif(char == '}'):
            answer += 1197
        elif(char == '>'):
            answer += 25137

    print("Part one answer is %s" % answer)

def part_two(lines):
    closing_chars = ")]}>"
    opening_chars = "([{<"

    chars_to_complete_lines = []
    incomplete_lines = []

    for line in lines:
        incomplete = True
        opened_chars = []
        for char in line:
            if(char in opening_chars):
                opened_chars.append(char)
            elif(char in closing_chars):
                char_to_close = opened_chars.pop()
                if(illegally_closed(char_to_close, char)):
                    incomplete = False
                    break

        if(incomplete and len(opened_chars) > 0):
            chars_to_complete_lines.append(complete_line(opened_chars))

    for line in chars_to_complete_lines:
        print(line)

    answers = []

    for missing_chars in chars_to_complete_lines:
        answer = 0
        missing_chars.reverse()

        for char in missing_chars:
            answer *= 5
            if(char == ')'):
                answer += 1
            elif(char == ']'):
                answer += 2
            elif(char == '}'):
                answer += 3
            elif(char == '>'):
                answer += 4
            else:
                print("Unxpected char received (%s) when calculating answer" % char)

        answers.append(answer)

    sorted_answers = sorted(answers)
    final_answer = sorted_answers[int(len(answers) / 2)]

    print("Part two answer is %s" % final_answer)

def get_input(filename):
    lines = []

    with open(filename) as file:
        lines = file.readlines()

    return lines

def illegally_closed(opened_char, closed_char):
    if(opened_char == '('):
        return closed_char != ')'
    elif(opened_char == '['):
        return closed_char != ']'
    elif(opened_char == '{'):
        return closed_char != '}'
    elif(opened_char == '<'):
        return closed_char != '>'

    print("Unexpected character %s %s" % (opened_char, closed_char))

puzzle_input = get_input("Day10PuzzleInput.txt")
part_one(puzzle_input)
part_two(puzzle_input)

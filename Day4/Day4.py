def part_one():
    bingo_numbers = None
    boards = []
    lines = []

    with open("Day4PuzzleInput.txt") as file:
       lines = file.readlines()

    bingo_numbers = lines[0].split(',')
    del lines[0]
    del lines [0]
    boards = create_boards(boards, lines)

    game_over = False

    while(game_over == False and len(bingo_numbers) > 0):
        number = bingo_numbers.pop(0)
        boards = mark_boards(boards, number)
        winning_board = check_for_win(boards)

        if(winning_board != None):
            game_over = True
            winning_value = calculate_value(winning_board)
            print(winning_value * int(number))

def part_two():
    bingo_numbers = None
    boards = []
    lines = []

    with open("Day4PuzzleInput.txt") as file:
       lines = file.readlines()

    bingo_numbers = lines[0].split(',')
    del lines[0]
    del lines [0]
    boards = create_boards(boards, lines)

    game_over = False

    print(str(len(boards)) + " boards")

    while(game_over == False and len(bingo_numbers) > 0):
        number = bingo_numbers.pop(0)
        boards = mark_boards(boards, number)

        non_winning_boards = []

        for board in boards:
            board_to_check = []
            board_to_check.append(board)

            winning_board = check_for_win(board_to_check)

            if(winning_board == None):
                non_winning_boards.append(board)
            elif(len(boards) == 1 and winning_board != None):
                game_over = True
                winning_value = calculate_value(board)
                print(winning_board)
                print(winning_value * int(number))
            else:
                print("board has won")

        boards = non_winning_boards

def calculate_value(board):
    winning_value = 0

    for line in board:
        for entry in line:
            value = int(entry)
            if(value != -1):
                winning_value += value

    return winning_value

def check_for_win(boards_list):
    winning_board = None

    for board in boards_list:
        board_length = len(board)
        for index in range(board_length):
            row = board[index]
            column = create_column(board, index)
            
            if(winning_row_or_column(row, column)):
                return board

    return None

def create_boards(boards_list, input_list):
    temp_board = []

    for line in input_list:
        if(len(line) > 1):
            board_row = line.split()
            temp_board.append(board_row)
        else:
            boards_list.append(temp_board)
            temp_board = []

    if(len(temp_board) > 1):
        boards_list.append(temp_board)

    return boards_list

def create_column(board, index):
    board_length = len(board)
    column = []

    for rows in range(board_length):
        column.append(board[rows][index])

    return column

def mark_boards(boards_list, number):
    for board in boards_list:
        for line in board:
            for index in range(len(line)):
                if int(line[index]) == int(number):
                    line[index] = -1

    return boards_list

def print_boards(boards_list):
    for board in boards_list:
        for line in board:
            print(line)

def winning_row_or_column(row, column):
    if(all(entry == -1 for entry in row)):
        return True

    if(all(entry == -1 for entry in column)):
        return True

    return False

part_one()
part_two()

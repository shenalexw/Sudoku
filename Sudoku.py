import random

board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

hard = 17
medium = 30
easy = 40


def clear(game):
    for row in range(len(game)):
        for column in range(len(game)):
            game[row][column] = 0


def print_board(game):
    for row in range(len(game)):
        if row % 3 == 0 and row != 0:
            print(" - - - - - + - - - - + - - - - - ")
        if row == 0:
            print(" - - - - - - - - - - - - - - - - ")
        for column in range(len(game)):
            if column % 3 == 0:
                print(" | ", end=" ")
            if column == 8:
                print(game[row][column], end="  | \n")
            else:
                print(str(game[row][column]) + " ", end="")
    print(" - - - - - - - - - - - - - - -  ")


def num_input(game, location, number):
    row = location[0]
    column = location[1]
    if check(game, location, number):
        game[row][column] = number
    else:
        return False


def check(game, location, number):
    row = location[0]
    column = location[1]
    row_box = (location[0] // 3) * 3
    column_box = location[1] // 3 * 3
    if game[row][column] != 0:
        return False
    for col_value in range(len(game)):
        if game[row][col_value] == number and column != col_value:
            return False
    for row_value in range(len(game)):
        if game[row_value][column] == number and row != row_value:
            return False
    for col_value in range(row_box, row_box + 3):
        for row_value in range(column_box, column_box + 3):
            if game[col_value][row_value] == number and (row_value, col_value) != location:
                return False
    return True


def find_zero(game):
    for row in range(len(game)):
        for column in range(len(game)):
            if game[row][column] == 0:
                return row, column
    return False


def solve(game):
    if not find_zero(game):
        return True

    else:
        row, column = find_zero(game)

    for num in range(1, 10):
        if check(game, (row, column), num):
            game[row][column] = num
            if solve(game):
                return True
            game[row][column] = 0
    return False


def ran_fill(game, counter=0):
    for row in range(len(game)):
        for column in range(len(game)):
            if game[row][column] == 0:
                num = random.randrange(1, 10)
                if check(game, (row, column), num):
                    counter += 1
                    num_input(game, (row, column), num)
            if counter >= 17:
                if not solve(game):
                    clear(game)
                    ran_fill(game, 0)
                else:
                    return None


def new_game(game, difficulty, counter=81):
    rem_num = difficulty
    for row in range(len(game)):
        for column in range(len(game)):
            if game[row][column] != 0 and counter >= rem_num:
                if random.randrange(2) == 0:
                    counter -= 1
                    game[row][column] = 0
            if counter <= rem_num:
                return None

    new_game(game, difficulty, counter)


def showcase_easy(game):
    ran_fill(game)
    new_game(board, easy)
    print("Problem:")
    print_board(game)
    print("Solution:")
    solve(board)
    print_board(game)


def showcase_medium(game):
    ran_fill(game)
    new_game(board, medium)
    print("Problem:")
    print_board(game)
    print("Solution:")
    solve(board)
    print_board(game)


def showcase_hard(game):
    ran_fill(game)
    new_game(board, hard)
    print("Problem:")
    print_board(game)
    print("Solution:")
    solve(board)
    print_board(game)


if __name__ == '__main__':
    showcase_easy(board)




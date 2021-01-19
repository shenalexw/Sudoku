import random
import time

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

hard = 25
medium = 38
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
    print(" - - - - - - - - - - - - - - - - ")


def num_input(game, location, number):
    row = location[0]
    column = location[1]
    if check(game, location, number):
        game[row][column] = number
        return True
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
                if num_input(game, (row, column), num):
                    counter += 1
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


def convert_time(given_seconds):
    minutes = given_seconds // 60
    seconds = given_seconds % 60
    return "%02d:%02d" % (minutes, seconds)


def generator(game, difficulty):
    go = True
    ran_fill(game)
    new_game(board, difficulty)
    print("Problem:")
    print_board(game)
    time_0 = time.time()
    while go:
        cont = input("Would you like to see the Solution? (yes/no): ")
        if cont.lower() == "yes":
            time_1 = time.time()
            stopwatch = time_1 - time_0
            display_time = convert_time(stopwatch)
            print("Solution:")
            solve(board)
            print_board(game)
            print("Nice Job!, It took you", display_time, "to complete the puzzle.")
            again_input = True
            while again_input:
                again = input("Would you like another puzzle? (yes/no)")
                if again.lower() == "yes":
                    generator(game, difficulty)
                    return
                elif again.lower() == "no":
                    go = False
                    again_input = False
                else:
                    print("Incorrect input, please try again!")
        elif cont.lower() == "no":
            time_1 = time.time()
            stopwatch = time_1 - time_0
            display_time = convert_time(stopwatch)
            print("Good Luck!, it has been:", display_time)
        else:
            print("Incorrect input, please try again!")


def solver(game):
    for rows in range(len(game)):
        for column in range(len(game)):
            correct_value = True
            while correct_value:
                print("Please input number in row ", rows + 1, "and column ", column + 1, "(type 'res' to restart)")
                num = input()
                if num.lower() == "res":
                    solver(game)
                    return
                elif not num.isdigit():
                    print("Incorrect input! Please input a number 0 - 9.")
                elif 9 >= int(num) >= 0:
                    game[rows][column] = int(num)
                    correct_value = False
                else:
                    print("Incorrect input! Please input a number 0 - 9.")
    print("The Problem:")
    print_board(game)
    after_input = True
    while after_input:
        cont = input("Is this correct? (yes/no)")
        if cont.lower() == "yes":
            if not find_zero(game):
                print("The Board is full already, Please try to input the puzzle again.")
                solver(game)
                return
            elif solve(game):
                print("The Solution:")
                print_board(game)
                input_run = True
                while input_run:
                    again = input("Would you like to input another puzzle? (yes/no)")
                    if again.lower() == "yes":
                        solver(game)
                        return
                    elif again.lower() == "no":
                        input_run = False
                        after_input = False
                    else:
                        print("Incorrect input, please try again.")
            else:
                print("Puzzle not Solvable! Please try to input the puzzle again.")
                solver(game)
                return
        elif cont.lower() == "no":
            print("Please try to input the numbers again.")
            solver(game)
            return
        else:
            print("Incorrect input, please try again.")


def main():
    main_run = True
    choice_run = True
    while main_run:
        choice = input("Would you like a Sudoku Puzzle, or would you like to use the solver? (puzzle / solver)")
        if choice.lower() == "solver":
            solver(board)
            main_run = False
        elif choice.lower() == "puzzle":
            while choice_run:
                level = input("Enter Difficulty (easy, medium, hard): ")
                if level.lower() == "easy":
                    generator(board, easy)
                    choice_run = False
                    main_run = False
                elif level.lower() == "medium":
                    generator(board, medium)
                    choice_run = False
                    main_run = False
                elif level.lower() == "hard":
                    generator(board, hard)
                    choice_run = False
                    main_run = False
                else:
                    print("Incorrect input, please try again!")
        else:
            print("Incorrect input, please try again!")


if __name__ == '__main__':
    main()

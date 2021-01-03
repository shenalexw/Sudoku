board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

"""
def solve(game):
"""


def print_board(game):
    for row in range(len(board)):
        if row % 3 == 0 and row != 0:
            print("=================================")
        for column in range(len(board)):
            if column % 3 == 0:
                print(" || ", end=" ")
            if column == 8:
                print(board[row][column], end="\n")
            else:
                print(str(board[row][column]) + " ", end="")


def num_input(location, number):
    row = location[0]
    column = location[1]
    if check(location, number):
        board[row][column] = number
    else:
        return "wrong move"


def check(location, number):
    row = location[0]
    column = location[1]
    row_box = (location[0] // 3) * 3
    column_box = location[1] // 3 * 3
    if board[row][column] != 0:
        return False
    for row_value in range(len(board)):
        if board[row][row_value] == number:
            return False
    for col_value in range(len(board)):
        if board[col_value][column] == number:
            return False
    for row_value in range(row_box, row_box + 3):
        for col_value in range(column_box, column_box + 3):
            if board[row_value][col_value] == number:
                return False
    return True

print(num_input((1,1), 1))
print_board(board)


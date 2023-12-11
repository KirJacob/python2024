import math


def get_cell_code(x, y):
    div_x = math.floor(x / 3)
    div_y = math.floor(y / 3)
    sub_square_code = 3 * div_x + div_y
    return sub_square_code


def validate_list(values):
    if len(values) != 9:
        return False
    for num in list(range(1, 10)):
        if num not in values:
            return False
    return True


def valid_solution(board):
    # validate rows
    for row_num in range(0, 9):
        if not validate_list(board[row_num]):
            return False

    # validate columns
    result = []
    for x in range(0, 9):
        column = []
        for y in range(0, 9):
            print(f"{board[x][y]} ", end="")
            column.append(board[y][x])
        result.append(column)
    for row_num in list(range(0, 9)):
        if not validate_list(result[row_num]):
            return False

    # validate sub-squares
    list_sub_squares = []
    for x in list(range(0, 9)):
        list_sub_squares.append([])
    for x in list(range(0, 9)):
        for y in list(range(0, 9)):
            cell_code = get_cell_code(x, y)
            list_sub_squares[cell_code].append(board_one[x][y])
    for sub_square_list in list_sub_squares:
        if not validate_list(sub_square_list):
            return False
    return True


# TESTS

board_one = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
             [6, 7, 2, 1, 9, 5, 3, 4, 8],
             [1, 9, 8, 3, 4, 2, 5, 6, 7],
             [8, 5, 9, 7, 6, 1, 4, 2, 3],
             [4, 2, 6, 8, 5, 3, 7, 9, 1],
             [7, 1, 3, 9, 2, 4, 8, 5, 6],
             [9, 6, 1, 5, 3, 7, 2, 8, 4],
             [2, 8, 7, 4, 1, 9, 6, 3, 5],
             [3, 4, 5, 2, 8, 6, 1, 7, 9]]

board_two = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
             [6, 7, 2, 1, 9, 0, 3, 4, 9],
             [1, 0, 0, 3, 4, 2, 5, 6, 0],
             [8, 5, 9, 7, 6, 1, 0, 2, 0],
             [4, 2, 6, 8, 5, 3, 7, 9, 1],
             [7, 1, 3, 9, 2, 4, 8, 5, 6],
             [9, 0, 1, 5, 3, 7, 2, 1, 4],
             [2, 8, 7, 4, 1, 9, 6, 3, 5],
             [3, 0, 0, 4, 8, 1, 1, 7, 9]]

print(valid_solution(board_one))
print(valid_solution(board_two))

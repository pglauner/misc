import itertools
import time

field0 = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 0]]

field1 = [[5, 0, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 0]]

field2 = [[0, 3, 4, 6, 7, 8, 9, 1, 2],
          [6, 7, 2, 1, 9, 5, 3, 0, 8],
          [1, 9, 8, 3, 4, 2, 5, 6, 7],
          [8, 5, 9, 7, 6, 1, 4, 2, 3],
          [4, 2, 6, 8, 5, 3, 7, 9, 1],
          [7, 1, 3, 9, 2, 4, 8, 5, 6],
          [9, 6, 1, 5, 3, 7, 2, 8, 4],
          [2, 8, 7, 4, 1, 9, 6, 3, 5],
          [3, 4, 5, 2, 8, 6, 1, 0, 0]]

solution = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]]

field_most_difficult_2010 = [[0, 0, 5, 3, 0, 0, 0, 0, 0],
                             [8, 0, 0, 0, 0, 0, 0, 2, 0],
                             [0, 7, 0, 0, 1, 0, 5, 0, 0],
                             [4, 0, 0, 0, 0, 5, 3, 0, 0],
                             [0, 1, 0, 0, 7, 0, 0, 6, 0],
                             [0, 0, 3, 2, 0, 0, 0, 8, 0],
                             [0, 6, 0, 5, 0, 0, 0, 0, 9],
                             [0, 0, 4, 0, 0, 0, 0, 3, 0],
                             [0, 0, 0, 0, 0, 9, 7, 0, 0]]

field_most_difficult_norvig1 = [[0, 0, 0, 0, 0, 6, 0, 0, 0],
                                [0, 5, 9, 0, 0, 0, 0, 0, 8],
                                [2, 0, 0, 0, 0, 8, 0, 0, 0],
                                [0, 4, 5, 0, 0, 0, 0, 0, 0],
                                [0, 0, 3, 0, 0, 0, 0, 0, 0],
                                [0, 0, 6, 0, 0, 3, 0, 5, 4],
                                [0, 0, 0, 3, 2, 5, 0, 0, 6],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0]]

field_most_difficult_norvig2 = [[0, 0, 0, 0, 0, 5, 0, 8, 0],
                                [0, 0, 0, 6, 0, 1, 0, 4, 3],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 1, 0, 5, 0, 0, 0, 0, 0],
                                [0, 0, 0, 1, 0, 6, 0, 0, 0],
                                [3, 0, 0, 0, 0, 0, 0, 0, 5],
                                [5, 3, 0, 0, 0, 0, 0, 6, 1],
                                [0, 0, 0, 0, 0, 0, 0, 0, 4],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0]]

field = field_most_difficult_norvig2

MAX = 9


def print_field():
    print repr(field).replace('], ', '\n').translate(None, '][,')


def solve_sudoku():
    return solve(0, 0)

def solve(row, col):
    if row > 8:
        return True
    if not field[row][col]:
        for val in range(1, 10):
            if check(row, col, val):
                field[row][col] = val
                # Solution found
                if next_cell(row, col):
                    return True
        # No solution -> revert
        field[row][col] = 0
    else:
        if next_cell(row, col):
            return True
    return False


def next_cell(row, col):
    if col == 8:
        return solve(row + 1, 0)
    else:
        return solve(row, col + 1)


def check(row, col, val):
    def get_subfield(x1, x2, y1, y2):
        return [item[x1:x2] for item in field[y1:y2]]

    def does_not_contain(l):
        if isinstance(l[0], int):
            return val not in l
        else:
            return val not in list(itertools.chain(*l))

    x_start = row - row % 3
    y_start = col - col % 3

    row_values = field[row]
    col_values = get_subfield(col, col+1, 0, MAX)
    square_values = get_subfield(y_start, y_start+3, x_start, x_start+3)

    return does_not_contain(row_values) \
            and does_not_contain(col_values) \
            and does_not_contain(square_values)

if __name__ == '__main__':
    print_field()
    start = time.clock()
    print solve_sudoku()
    t = time.clock() - start
    print_field()
    print '(%.2f seconds)\n' % t

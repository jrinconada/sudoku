import validator

def solve(sudoku):
    for y in range(len(sudoku)):
        for x in range(len(sudoku[0])):        
            if sudoku[y][x] == 0:
                for n in range(1, len(sudoku) + 1):
                    if validator.possible(sudoku, n, x, y):
                        sudoku[y][x] = n
                        if solve(sudoku):
                            return True
                        sudoku[y][x] = 0 # Not solved with this number
                return False # Not solved with any number
    return True
    
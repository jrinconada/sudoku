import validator

def solve(sudoku):       
    for x in range(len(sudoku[0])):
        for y in range(len(sudoku)):
            if sudoku[x][y] == 0:
                for n in range(len(sudoku)):
                    if validator.possible(sudoku, n, x, y):
                        sudoku[x][y] = n
                        solve(sudoku)
                        sudoku[x][y] = 0 # Not solved with this number
                return # Not solved with any number
    
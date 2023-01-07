import validator

def solve(sudoku):
    global sudoku
    solve()    

def solve():
    global sudoku    
    for x in range(len(sudoku[0])):
        for y in range(len(sudoku)):
            if sudoku[x][y] == 0:
                for n in range(len(sudoku)):
                    if validator.valid(sudoku, x, y, n):
                        sudoku[x][y] = n
                        solve()
                        sudoku[x][y] = 0 # Not solved with this number
                return # Not solved with any number
    
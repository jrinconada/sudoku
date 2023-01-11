import validator
import output

fails = 0

def solve(sudoku, display_progress = False):
    global fails
    for y in range(len(sudoku)):
        for x in range(len(sudoku[0])):        
            if sudoku[y][x] == 0:
                for number in range(1, len(sudoku) + 1):
                    if display_progress:
                        output.diplay(number, x, y)
                    if validator.possible(sudoku, number, x, y):
                        sudoku[y][x] = number
                        if solve(sudoku, display_progress):
                            return True
                        sudoku[y][x] = 0 # Not solved with this number
                        fails = fails + 1
                        if display_progress:
                            output.delete(x, y)
                    else:
                        fails = fails + 1
                        if display_progress:
                            output.delete(x, y)
                return False # Not solved with any number
            else:
                if display_progress:
                    output.diplay(sudoku[y][x], x, y)
    return True
    
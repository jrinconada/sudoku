import random
import validator
import output

def generate(n = 9, display_progress = False):
    """ Generate a random matrix of numbers of n by n (9 by default)"""
    global fails
    fails = 0
    sudoku = [[0 for x in range(n)] for y in range(n)]
    fill(sudoku, 0, 0, display_progress)
    return sudoku
    
def fill(sudoku, x = 0, y = 0, display_progress = False):
    global fails
    possibilities = list(range(1, len(sudoku) + 1))    
    random.shuffle(possibilities)    
    for number in possibilities:
        if display_progress:
            output.diplay(number, x, y)
        if validator.possible(sudoku, number, x, y):
            sudoku[y][x] = number            
            if y == len(sudoku) - 1 and x == len(sudoku[0]) - 1:
                return True # If we arrive at the end of the sudoku, it means that all cells are filled            
            filled = fill(sudoku, x + 1 if x < len(sudoku[y]) - 1 else 0, y + 1 if x == len(sudoku[y]) - 1 else y, display_progress)
            if filled:
                return True # If filled is true, it means that one of the steps have filled the last cell
            sudoku[y][x] = 0
            if display_progress:
                output.delete(x, y)
        else:
            fails = fails + 1
            if display_progress:
                output.delete(x, y)
    return False # If we are here, there was no possible number to put in that space, so we need to go back to the previous step

def removeNumber(sudoku):    
    x = random.randint(0, len(sudoku) - 1)
    y = random.randint(0, len(sudoku) - 1)
    while sudoku[y][x] == 0:
        x = random.randint(0, len(sudoku) - 1)
        y = random.randint(0, len(sudoku) - 1)
    sudoku[y][x] = 0
    
import random
import validator

def generate(n = 9):
    """ Generate a random matrix of numbers of n by n (9 by default)"""
    sudoku = [[0 for x in range(n)] for y in range(n)]
    fill(sudoku)    
    return sudoku
    
def fill(sudoku, x = 0, y = 0):        
    possibilities = list(range(1, 10))
    random.shuffle(possibilities)    
    for number in possibilities:
        if validator.possible(sudoku, number, x, y):
            sudoku[y][x] = number
            if y == len(sudoku) - 1 and x == len(sudoku[0]) - 1:
                return True # If we arrive at the end of the sudoku, it means that all cells are filled            
            filled = fill(sudoku, x + 1 if x < len(sudoku[y]) - 1 else 0, y + 1 if x == len(sudoku[y]) - 1 else y)
            if filled:
                return True # If filled is true, it means that one of the steps have filled the last cell
            sudoku[y][x] = 0
    return False # If we are here, there was no possible number to put in that space, so we need to go back to the previous step
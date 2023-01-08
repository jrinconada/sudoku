import random
import validator

def generate(n = 9):
    """ Generate a random matrix of numbers of n by n (9 by default)"""
    sudoku = [[0 for x in range(n)] for y in range(n)]
    fill(sudoku)    
    return sudoku
    
def fill(sudoku, x = 0, y = 0):        
    row = list(range(1, 10))
    random.shuffle(row)    
    for n in row:
        if y == 0 or validator.possible(sudoku, n, x, y): # No need to check first row
            sudoku[y][x] = n            
            fill(sudoku, x + 1 if x < len(sudoku[y]) else 0, y + 1 if x == len(sudoku[y]))
    if len(row) == 0: # This row is filled 
        if y < len(sudoku) - 1: # There are still empty rows
            fill(sudoku, 0, y + 1)
    else: # This row cannot be filled with this list of numbers, we need to try another one
        fill(sudoku, 0, y)
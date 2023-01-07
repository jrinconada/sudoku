import random
import validator

def generate(n=9):
    """ Generate a random matrix of numbers of n by n (9 by default)"""
    sudoku = [[0 for x in range(n)] for y in range(n)]
    # for i in range(n):
    #     row = list(range(1, n + 1))
    #     random.shuffle(row)
    #     sudoku.append(row)
    fill(sudoku)    
    return sudoku
    
def fill(sudoku):
    for x in range(9):
        row = list(range(1, 10))
        random.shuffle(row)
        for y in range(9):
            for n in row:
                if x == 0 or validator.possible(sudoku, n, x, y): # No need to check first row
                    sudoku[x][y] = n
                    row.remove(n)
                    break
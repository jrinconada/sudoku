import random

def generate(n=9):
    """ Generate a random matrix of numbers of n by n (9 by default)"""
    sudoku = []
    for i in range(n):
        row = list(range(1, n + 1))
        random.shuffle(row)
        sudoku.append(row)
    return sudoku
    
    
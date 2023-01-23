
def validate(sudoku):
    # Row validation
    for row in sudoku:
        if not valid(row):
            return False
    
    # Column validation
    for column in list(zip(*sudoku)):
        if not valid(column):    
            return False
    
    # Square validation
    square_size = int(len(sudoku) ** (1/2))
    for n in range(0, len(sudoku), square_size):
        for m in range(0, len(sudoku), square_size):
            square = []
            for i in range(square_size):
                for j in range(square_size):
                    square.append(sudoku[i+n][j+m])
            if not valid(square):
                return False
                
    return True
    
def valid(items):
    """ Given a row, colum or square, return if they are valid. """
    numbers = set(range(1, len(items) + 1))
    for number in items:
        if not number in numbers:
            return False
        numbers.remove(number)
    return len(numbers) == 0

def possible(sudoku, number, x, y):
    """ Given a sudoku, a number and position, return if that number can be in that position. """
    square_size = int(len(sudoku) ** (1/2))
    for i in range(len(sudoku)):
        if number == sudoku[y][i]: # Check row
            return False
        if number == sudoku[i][x]: # Check column
            return False
        if number == sudoku[i // square_size + y // square_size * square_size][i % square_size + x // square_size * square_size]: # Check square
            return False
    return True
    

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
            fails = fails + 1
            if display_progress:
                output.delete(x, y)
        else:
            fails = fails + 1
            if display_progress:
                output.delete(x, y)
    return False # If we are here, there was no possible number to put in that space, so we need to go back to the previous step

def remove_number(sudoku):    
    x = random.randint(0, len(sudoku) - 1)
    y = random.randint(0, len(sudoku) - 1)
    while sudoku[y][x] == 0:
        x = random.randint(0, len(sudoku) - 1)
        y = random.randint(0, len(sudoku) - 1)
    sudoku[y][x] = 0
    
def swap_numbers(sudoku, a, b):
    for y in range(len(sudoku)):
        for x in range(len(sudoku[0])):
            if sudoku[y][x] == a:
                sudoku[y][x] = b
            elif sudoku[y][x] == b:
                sudoku[y][x] = a

def swap_rows(sudoku, y1, y2):
    row1 = sudoku[y1].copy()
    sudoku[y1] = sudoku[y2]
    sudoku[y2] = row1

def swap_columns(sudoku, x1, x2):
    for y in range(len(sudoku)):
        column1 = sudoku[y][x1]
        sudoku[y][x1] = sudoku[y][x2]
        sudoku[y][x2] = column1

def transpose(sudoku):
    temp = [row[:] for row in sudoku] # Deep copy of sudoku
    for i in range(len(sudoku)):
        for j in range(len(sudoku[0])):
            sudoku[i][j] = temp[j][i]

def roll(sudoku):
    """Counterclockwise 90º rotation"""
    temp = [row[:] for row in sudoku] # Deep copy of sudoku
    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            sudoku[i][j] = temp[j][len(sudoku[i]) - 1 - i]

def apply_varitiations(sudoku):
    # Transpose or not ?
    if random.choice([True, False]):
        print('Transposing...')
        transpose(sudoku)
    # Roll 0º, 90º, 180º, 270º ?
    degrees = random.choice([0, 90, 180, 270])
    if degrees != 0: 
        print('Rolling', degrees, 'degrees...')
    for rolling_times in range(degrees // 90):
        roll(sudoku)

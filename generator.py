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

def swap_horizontal_blocks(sudoku, x1, x2):
    square_size = int(len(sudoku) ** (1/2))
    temp = [row[:] for row in sudoku] # Deep copy of sudoku
    for i in range(square_size):
        for j in range(len(sudoku[i])):
            sudoku[i + x1 * square_size][j] = temp[i + x2 * square_size][j]
            sudoku[i + x2 * square_size][j] = temp[i + x1 * square_size][j]

def swap_vertical_blocks(sudoku, y1, y2):
    square_size = int(len(sudoku) ** (1/2))
    temp = [row[:] for row in sudoku] # Deep copy of sudoku
    for i in range(square_size):
        for j in range(len(sudoku[i])):
            sudoku[j][i + y1 * square_size] = temp[j][i + y2 * square_size]
            sudoku[j][i + y2 * square_size] = temp[j][i + y1 * square_size]

def transpose(sudoku):
    temp = [row[:] for row in sudoku] # Deep copy of sudoku
    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            sudoku[i][j] = temp[j][i]

def roll(sudoku):
    """Counterclockwise 90º rotation"""
    temp = [row[:] for row in sudoku] # Deep copy of sudoku
    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            sudoku[i][j] = temp[j][len(sudoku[i]) - 1 - i]

def apply_variations(sudoku):
    # Generate all possible pairs of numbers for this sudoku size
    pairs = all_pairs_of_numbers(len(sudoku))
    # Apply swap of numbers 1 and 2, 1 and 3, 1 and 4... or not?
    for i, apply in enumerate(random.choices([True, False], k = len(pairs))):
        if apply:
            print('Swaping', pairs[i][0] + 1, 'and', pairs[i][1] + 1, '...')
            swap_numbers(sudoku, pairs[i][0] + 1, pairs[i][1] + 1)
    # Generate all possible pairs of numbers for this sudoku square size
    square_size = int(len(sudoku) ** (1/2))
    pairs = all_pairs_of_numbers(square_size)
    # Apply swap of rows 1 and 2, 1 and 3, 4 and 5... or not?
    for s in range(0, len(sudoku), square_size):
        for i, apply in enumerate(random.choices([True, False], k = len(pairs))):
            print(i + s)
            if apply:
                print('Swaping rows', pairs[i][0] + s, 'and', pairs[i][1] + s, '...')
                swap_rows(sudoku, pairs[i][0] + s, pairs[i][1] + s)
    # Apply swap of columns 1 and 2, 1 and 3, 4 and 5... or not?
    for s in range(0, len(sudoku), square_size):
        for i, apply in enumerate(random.choices([True, False], k = len(pairs))):
            if apply:
                print('Swaping columns', pairs[i][0] + s, 'and', pairs[i][1] + s, '...')
                swap_columns(sudoku, pairs[i][0] + s, pairs[i][1] + s)
    # Apply swap of horizontal blocks 1 and 2, 1 and 3, 2 and 3... or not?    
    for i, apply in enumerate(random.choices([True, False], k = len(pairs))):
        if apply:
            print('Swaping horizontal blocks', pairs[i][0], 'and', pairs[i][1], '...')
            swap_horizontal_blocks(sudoku, pairs[i][0], pairs[i][1])
    # Apply swap of vertical blocks 1 and 2, 1 and 3, 2 and 3... or not?
    for i, apply in enumerate(random.choices([True, False], k = len(pairs))):
        if apply:
            print('Swaping vertical blocks', pairs[i][0], 'and', pairs[i][1], '...')
            swap_vertical_blocks(sudoku, pairs[i][0], pairs[i][1])
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

def all_pairs_of_numbers(n):
    pairs = []
    numbers = set(range(n))

    while len(numbers) != 0:
        number = numbers.pop()
        for j in numbers:
            pairs.append((number, j))
    return pairs

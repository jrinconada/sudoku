
import time

DELAY = .025

def show(sudoku):
    print()
    x = 1
    for row in sudoku:
        y = 1
        for column in row:
            if column == 0:
                print(' ', end=' ')
            else:
                print(column, end=' ')
            if y == 3:
                print('  ', end='')
                y = 0
            y = y + 1
        if x == 3:
            print()
            x = 0
        x = x + 1
        print()

def diplay(number, x, y):
    if x == 0: # Next line
        print()
    if x == 3 or x == 6: # Horizontal square space
        print('  ', end='')
    if x == 0 and (y == 3 or y == 6): # Vertical square space
        print()
    print(number, end=' ', flush=True) # Print number    
    time.sleep(DELAY) # Delay

def delete(x, y):
    print('\b\b \b', end='', flush=True) # Remove the number
    if x == 0: # Remove next line
        print('\033[F', end='', flush=True)
    if x == 0 and (y == 3 or y == 6): # Remove vertical square space
        print('\033[F', end='', flush=True)    
    if x == 3 or x == 6: # Remove horizontal square space
        print('\b\b', end='', flush=True)
    time.sleep(DELAY) # Delay

def save(sudoku):
    result = ''    
    for row in sudoku:
        result = result + ''.join(str(n) for n in row)
    write('out.txt', result)

def write(location, data):
    """ Given a file path and some data, saves the data to the file.
        Automatically creates the file if it does not exit and overwrites the content if there is something """
    with open(location, 'a') as file:
        file.write(data)
            

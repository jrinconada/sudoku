
def show(sudoku):
    print()
    x = 1
    for row in sudoku:
        y = 1    
        for column in row:
            print(column, end=' ')
            if y == 3:
                print(' ', end=' ')
                y = 0
            y = y + 1
        if x == 3:
            print()
            x = 0
        x = x + 1
        print()

def save(sudoku):
    result = ''    
    for row in sudoku:
        result = result + ''.join(str(n) for n in row)
    write('out.txt', result)

def write(location, data):
    """ Given a file path and some data, saves the data to the file.
        Automatically creates the file if it does not exit and overwrites the content if there is something """
    with open(location, 'w') as file:
        file.write(data)
            

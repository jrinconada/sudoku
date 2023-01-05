
def show(sudoku):
    for row in sudoku:
        print('|', end='')
        for column in row:
            print(column, end='|')
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
            

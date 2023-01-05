
def show(sudoku):
    for row in sudoku:
        print('|', end='')
        for column in row:
            print(column, end='|')
        print()
            

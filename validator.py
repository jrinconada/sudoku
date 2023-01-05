
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
    for n in range(0,7,3):
        for m in range(0,7,3):
            square = []
            for i in range(3):
                for j in range(3):
                    square.append(sudoku[i+n][j+m])
            if not valid(square):
                return False
                
    return True
    
def valid(items):
    numbers = set(range(1, len(items) + 1))
    for number in items:
        if not number in numbers:
            return False
        numbers.remove(number)
    return len(numbers) == 0

        
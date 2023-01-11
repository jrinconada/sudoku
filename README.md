# :crossed_flags: Sudoku
**Generation**, **validation** and **solving** *Sudokus*.

Sorry, **not** for **playing** XD. :stuck_out_tongue_closed_eyes:

## Generator
Creating a list of random numbers from *1* to *9* and trying them to generate a grid following *sudoku* rules using a *backtracking* and *recursion*.
![](generation.gif)

```python
def fill(sudoku, x = 0, y = 0):    
    possibilities = list(range(1, len(sudoku) + 1))    
    random.shuffle(possibilities)    
    for number in possibilities:        
        if validator.possible(sudoku, number, x, y):
            sudoku[y][x] = number            
            if y == len(sudoku) - 1 and x == len(sudoku[0]) - 1:
                return True # If we arrive at the end of the sudoku, it means that all cells are filled            
            filled = fill(sudoku, x + 1 if x < len(sudoku[y]) - 1 else 0, y + 1 if x == len(sudoku[y]) - 1 else y) # Recursive call
            if filled:
                return True # If filled is true, it means that one of the steps have filled the last cell
            sudoku[y][x] = 0    
    return False # If we are here, there was no possible number to put in that space, so we need to go back to the previous step (backtracking)
```

## Solver
Trying the numbers from *1* to *9* to fill the grid following *sudoku* rules using a *backtracking* and *recursion*.
![](solving.gif)

```python
def solve(sudoku):
    for y in range(len(sudoku)):
        for x in range(len(sudoku[0])):        
            if sudoku[y][x] == 0:
                for number in range(1, len(sudoku) + 1):
                    if display_progress:
                        output.diplay(number, x, y)
                    if validator.possible(sudoku, number, x, y):
                        sudoku[y][x] = number
                        if solve(sudoku, display_progress): # Recursive call
                            return True
                        sudoku[y][x] = 0 # Not solved with this number                    
                return False # Not solved with any number (back track!)
    return True
```
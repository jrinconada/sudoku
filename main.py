import generator
import validator
import output
import time
import solver

NUMBER_OF_SUDOKUS = 1
SHOW_GENERATION_PROCESS = False
SHOW_SOLVING_PROCESS = True
SIZE = 9
SPACES = 24 # 24 beginner, 53 expert (for a 9x9 grid)

total = 0
start = time.time()

for i in range(NUMBER_OF_SUDOKUS):
    # Generation of filled sudoku
    sudoku = generator.generate(SIZE, SHOW_GENERATION_PROCESS)
    if not SHOW_GENERATION_PROCESS:
        output.show(sudoku)    
    valid = validator.validate(sudoku)
    total = total + generator.fails
    print('\n\nThis is a', 'valid' if valid else 'invalid', 'sudoku.', generator.fails, 'failed tries. Average:', total / (i + 1), 'tries. Total:', total, 'tries.')

    # Remove numbers
    for s in range(SPACES):    
        generator.removeNumber(sudoku)
    output.show(sudoku)
    output.save(sudoku)

    # Solve sudoku
    solver.solve(sudoku, SHOW_SOLVING_PROCESS)    
    if not SHOW_SOLVING_PROCESS:
        output.show(sudoku)
    print('\n\nSudoku solved. It took', solver.fails, 'tries.')

# Show summary
print(NUMBER_OF_SUDOKUS, 'sudoku generated and solved in', round(time.time() - start), 'seconds.')
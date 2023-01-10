import generator
import validator
import output
import time
import solver

NUMBER_OF_SUDOKUS = 100
SHOW_GENERATION = False
SIZE = 9
SPACES = 53 # 24 beginner, 53 expert (for a 9x9 grid)

total = 0
start = time.time()

for i in range(NUMBER_OF_SUDOKUS):
    sudoku = generator.generate(SIZE, SHOW_GENERATION)
    if not SHOW_GENERATION:
        output.show(sudoku)    
    valid = validator.validate(sudoku)
    total = total + generator.fails
    print('\n\nThis is a', 'valid' if valid else 'invalid', 'sudoku.', generator.fails, 'failed tries. Average:', total / (i + 1), 'tries. Total:', total, 'tries.')
    for s in range(SPACES):    
        generator.removeNumber(sudoku)
    output.show(sudoku)
    output.save(sudoku)
    solver.solve(sudoku)
    output.show(sudoku)

print('It took', time.time() - start, 'seconds.')
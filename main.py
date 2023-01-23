import generator
import validator
import output
import time
import solver

NUMBER_OF_SUDOKUS = 1
SHOW_GENERATION_PROCESS = False
SHOW_SOLVING_PROCESS = False
FIND_ALL_SOLUTIONS = False
SIZE = 9 # Must be a perfect square: 4, 9, 16 ...
SPACES = 24 # 24 beginner, 37 easy, 50 medium, 53 hard, 59 evil (for a 9x9 grid)

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

    # Apply variations
    generator.apply_variations(sudoku)
    output.show(sudoku)
    valid = validator.validate(sudoku)
    print('\n\nThis is a', 'valid' if valid else 'invalid', 'sudoku.')

    # Remove numbers
    for s in range(SPACES):    
        generator.remove_number(sudoku)
    output.show(sudoku)
    output.save(sudoku)

    # Solve sudoku
    solver.solve(sudoku, SHOW_SOLVING_PROCESS, FIND_ALL_SOLUTIONS)    
    if not SHOW_SOLVING_PROCESS:
        output.show(sudoku)
    print('\n\nSudoku with',SPACES , 'spaces solved. It took', solver.fails, 'tries and has', solver.solutions, 'solutions.')
    solver.solutions = 0

# Show summary
print(NUMBER_OF_SUDOKUS, 'sudoku generated and solved in', round(time.time() - start), 'seconds.')

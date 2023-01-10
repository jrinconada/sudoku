import generator
import validator
import output
import time

NUMBER_OF_SUDOKUS = 1
total = 0
start = time.time()

for i in range(NUMBER_OF_SUDOKUS):
    sudoku = generator.generate(9, True)    
    output.save(sudoku)
    valid = validator.validate(sudoku)
    total = total + generator.fails
    print('\n\nThis is a', 'valid' if valid else 'invalid', 'sudoku.', generator.fails, 'failed tries. Average:', total / (i + 1), 'tries. Total:', total, 'tries.')

print('It took', time.time() - start, 'seconds.')
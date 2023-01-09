import generator
import validator
import output
import time

total = 0
start = time.time()

for i in range(100):
    sudoku = generator.generate()
    output.show(sudoku)
    output.save(sudoku)
    valid = validator.validate(sudoku)
    total = total + generator.fails
    print('This is a', 'valid' if valid else 'invalid', 'sudoku.', generator.fails, 'failed tries. Average:', total / (i + 1), 'tries. Total:', total, 'tries.')

print('It took', time.time() - start, 'seconds.')
     

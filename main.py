import generator
import validator
import output

sudoku = generator.generate()
output.show(sudoku)
output.save(sudoku)
valid = validator.validate(sudoku)
print('Valid sudoku' if valid else 'Invalid sudoku')

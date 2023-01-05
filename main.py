import generator
import validator
import output

def usage():
    return """
    USAGE: main.py [number of sudokus] [-o out.txt]

    1. If no number is given, it will generate one sudoku
    2. If no output file is given, it will write to the console    

    EXAMPLES: 
        - 20 sudokus saved in a text file: main.py 20 -o sudokus.txt"""

sudoku = generator.generate()
output.show(sudoku)
output.save(sudoku)
valid = validator.validate(sudoku)
print('Valid sudoku' if valid else 'Invalid sudoku')

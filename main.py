import generator
import output

def usage():
    return """
    USAGE: main.py [number of sudokus] [-o out.txt]

    1. If no number is given, it will generate one sudoku
    2. If no output file is given, it will write to the console    

    EXAMPLES: 
        - 20 sudokus saved in a text file: main.py 20 -o sudokus.txt"""

output.show(generator.generate())

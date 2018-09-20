# This file contains all the class definitions pertinent to the game

import numpy as np

puzzle1 = {'level' : 'beginner',
           'width': 7,
           'height': 7,
           'col_hints' : np.array(
               [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                ['3', '5', '5', '5', '5', '5', '3']]
                ),
            'row_hints' : np.array(
                [[' ', '1', '1'],
                 [' ', '3', '3'],
                 [' ', ' ', '7'],
                 [' ', ' ', '7'],
                 [' ', ' ', '5'],
                 [' ', ' ', '3'],
                 [' ', ' ', '1']]
                 )
            }


def init_grid(puzzleID):
    width = puzzleID['width']
    row_hints = puzzleID['row_hints']
    #col_hints = puzzleID['col_hints']
    col_divide = [' ', ' ', ' ', ' ', ' ', '|'] + ['-', '|'] * width
    init_row1 = [row_hints[0,0], ' ', row_hints[0,1], ' ', row_hints[0,2], '|']  + ['.', '|'] * width
    init_row2 = [row_hints[1,0], ' ', row_hints[1,1], ' ', row_hints[1,2], '|']  + ['.', '|'] * width
    init_row3 = [row_hints[2,0], ' ', row_hints[2,1], ' ', row_hints[2,2], '|']  + ['.', '|'] * width
    init_row4 = [row_hints[3,0], ' ', row_hints[3,1], ' ', row_hints[3,2], '|']  + ['.', '|'] * width
    init_row5 = [row_hints[4,0], ' ', row_hints[4,1], ' ', row_hints[4,2], '|']  + ['.', '|'] * width
    init_row6 = [row_hints[5,0], ' ', row_hints[5,1], ' ', row_hints[5,2], '|']  + ['.', '|'] * width
    init_row7 = [row_hints[6,0], ' ', row_hints[6,1], ' ', row_hints[6,2], '|']  + ['.', '|'] * width
    grid = np.array([col_divide, init_row1, init_row2, init_row3, init_row4, init_row5, init_row6, init_row7])
    return grid

class game():
    '''Initializes game object. A game is the complete grid of the puzzle, which can vary is size depending on the difficulty. '''

    def __init__(self, puzzleID):
        self.gameID = puzzleID
        self.complete = False
        self.level = puzzleID['level']  # beginner = 7x7, easy = 10x10, medium = 15x15, difficult = 20x20. Level info stored under gameID in database.
        self.width = puzzleID['width'] 
        self.row_hints = puzzleID['row_hints']   # array of clue strings for the rows. Stored under gameID in database. 
        self.col_hints = puzzleID['col_hints']   # array of clue strings for the columns. Stored under gameID in database. 
        self.grid = init_grid(puzzleID)

    def print_grid(self, grid):
        for crow in self.col_hints:
            print('     |', end='')
            for item in crow:
                print(item + '|', end='')
            print()
        for row in grid:
                for el in row:
                    print(el, end='')
                print()

    def insert_fill(self, grid, x, y):
        grid[(x, y * 2 + 4)] = '#'
        self.print_grid(grid)

    def complete_puzzle(self):
        self.complete = True
        return self.complete

# GAME

game1 = game(puzzle1)
print(' -------------------------------')
print('/ Welcome to Becca\'s Nonogram! /')
print('-------------------------------')
print()
quit_game = False
print('Your first challenge, is to find the secret message hidden in the puzzle below!')
print(game1.level)
print()
game1.print_grid(game1.grid)
print()
while not game1.complete and not quit_game:
    print('Please continue to solve!')
    print()
    option = input('To make a (m)ove, press m. To (q)uit the game, press q. ')
    if option == 'q':
        print()
        print('Bye-Bye for now!')
        quit_game = True
    else:
        x = int(input('Please enter the row of the cell you want to fill in: '))
        y = int(input('Please enter the column of the cell you want to fill in: '))
        print(game1.insert_fill(game1.grid, x, y))
print()
if game1.complete == True:
    print('Congratulations! You\'ve uncovered the hidden message!')

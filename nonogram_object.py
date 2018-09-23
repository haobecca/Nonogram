from grid_object.main import Grid

FILENAME = "./puzzles/puzzle1.grd"

class Nonogram(Grid):

    def __init__(self, fname):
        super().__init__(input_str=fname)

    def _make_empty_puzzle(self):
        self._grid = [list('0' * len(line)) for line in self._grid]
        return self._grid

def main():
    grid_solution = Nonogram(FILENAME)
    print(grid_solution)
    grid_non = Nonogram(FILENAME)
    print(grid_non)
    '''
    grid_non._make_empty_puzzle()
    print(grid_non)
    print('The value in cell (1,1) is ', grid_non.get_value(0, 0))
    grid_non.set_value(0, 0, "1")
    print(grid_non)
    print('The value in cell (1,1) is ', grid_non.get_value(0, 0))
    '''
    def check_solution(grid, solution):
        if grid == solution:
            print('You are correct!')
        else:
            print('Please try again!')
    check_solution(grid_non._grid, grid_solution._grid)

if __name__ == '__main__':
    main()
from utils import *


def solve():
    sudoku_input = input('''Enter sudoku's numbers like example (use a '.' as a placeholder for an empty box)
(Ex. '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3)
''')
    display(search(grid_values(sudoku_input)))


if __name__ == '__main__':
    solve()

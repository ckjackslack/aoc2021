from _04_giant_squid import (load_data, sum_all_unmarked, is_board_winning,
    set_drawn_number)
from aoc_helpers import get_current_input_file
from pprint import pprint
from collections import OrderedDict

def main():
    drawn_numbers, boards = load_data(get_current_input_file())
    drawn_numbers = iter(drawn_numbers)
    winning_boards = OrderedDict()
    while True:
        try:
            n = next(drawn_numbers)
            for board in boards:
                board = set_drawn_number(board, n)
            for i, board in enumerate(boards):
                if is_board_winning(board):
                    last_number = n
                    unmarked_sum = sum_all_unmarked(board)
                    res = last_number * unmarked_sum
                    if i not in winning_boards:
                        winning_boards[i] = res
        except StopIteration:
            break
    print(winning_boards)

if __name__ == '__main__':
    main()
from random import shuffle, randint
from pprint import pprint
from dataclasses import dataclass, field
from typing import List

from aoc_helpers import get_current_input_file

N_COLS = 5

@dataclass
class Number:
    value: int
    is_marked: bool = field(default = False)
    def __repr__(self):
        return str(self.value)

def generate_board(num_range = 25, n_cols = 5) -> List[List[Number]]:
    bingo_board = list(range(num_range))
    bingo_board = list(map(Number, bingo_board))
    shuffle(bingo_board)
    bingo_board = [
        bingo_board[i:i+n_cols]
        for i
        in range(0, len(bingo_board), n_cols)
    ]
    return bingo_board

def is_board_winning(board, n_cols = 5) -> bool:
    for row in board:
        if all([c.is_marked for c in row]):
            return True
    for i in range(n_cols):
        if all([r[i].is_marked for r in board]):
            return True
    return False

def sum_all_unmarked(board) -> int:
    tally = 0
    for row in board:
        for column in row:
            if not column.is_marked:
                tally += column.value
    return tally

def set_drawn_number(board, number: int) -> List[List[Number]]:
    found = False
    for i, row in enumerate(board):
        for j, column in enumerate(row):
            if column.value == number:
                board[i][j].is_marked = True
                found = True
                break
        if found:
            break
    return board

def generate_boards(n_times = 10):
    boards = []
    for _ in range(n_times):
        boards.append(generate_board())
    return boards

def draw_number():
    generated_so_far = set()
    while len(generated_so_far) < 25:
        n = randint(0, 24)
        if n not in generated_so_far:
            generated_so_far.add(n)
            yield n

# def main():
#     dn = draw_number()
#     boards = generate_boards()
#     ns = []
#     while True:
#         try:
#             n = next(dn)
#             ns.append(n)
#             print(ns)
#             for i, board in enumerate(boards, start = 1):
#                 board = set_drawn_number(board, n)
#                 if is_board_winning(board):
#                     last_number = n
#                     unmarked_sum = sum_all_unmarked(board)
#                     print(last_number * unmarked_sum)
#                     # print(n)
#                     # print(f'Board #{i} won')
#                     pprint([[(col.is_marked) for col in row] for row in board])
#                     exit()
#         except StopIteration:
#             break

def load_data(filename):
    drawn_numbers = None
    boards = []
    with open(filename) as f:
        drawn_numbers = [int(n) for n in next(f).strip().split(',')]
        board = []
        for line in f:
            line = line.strip()
            if line:
                line = [Number(int(n)) for n in line.split()]
                board.append(line)
            else:
                if board:
                    boards.append(board)
                board = []
    return drawn_numbers, boards

def check_flags(board):
    pprint([[col.is_marked for col in row] for row in board])

def check_vals(board):
    pprint([[col for col in row] for row in board])

def main():
    drawn_numbers, boards = load_data(get_current_input_file())
    drawn_numbers = iter(drawn_numbers)
    while True:
        try:
            n = next(drawn_numbers)
            for board in boards:
                board = set_drawn_number(board, n)
            for board in boards:
                if is_board_winning(board):
                    last_number = n
                    unmarked_sum = sum_all_unmarked(board)
                    print(last_number * unmarked_sum)
                    exit()
        except StopIteration:
            break

if __name__ == '__main__':
    main()
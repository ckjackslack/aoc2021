from _02_dive import ExtraPosition, calculate_final_position
from aoc_helpers import fcommands

def main():
    # e_pos = ExtraPosition(debug = True)
    e_pos = ExtraPosition()
    e_pos = calculate_final_position(e_pos, fcommands())
    print(e_pos)
    print(e_pos.get_result())

if __name__ == '__main__':
    main()
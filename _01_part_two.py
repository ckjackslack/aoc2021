from _01_sonar_sweep import larger_than_previous_measurement
from aoc_helpers import (get_numbers_from_sliding_window,
    get_current_input_file, get_numbers_generator, sum_sublists)

def main():
    nums_gen = get_numbers_generator(get_current_input_file())
    nums_gen = get_numbers_from_sliding_window(list(nums_gen))
    nums_gen = sum_sublists(nums_gen)
    print(larger_than_previous_measurement(nums_gen, 'sum'))

if __name__ == '__main__':
    main()
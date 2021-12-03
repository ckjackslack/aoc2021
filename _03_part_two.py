from aoc_helpers import fcommands
from _03_binary_diagnostic import (get_column_wise_list,
    get_most_common_bit)

def keep_with_position_having_bit(bin_nums, position, bit):
    for bin_num in bin_nums:
        if bin_num[position] == bit:
            yield bin_num

def check_bit_for_oxygen(bin_nums, position):
    bits = list(get_column_wise_list(bin_nums, position))
    return get_most_common_bit(bits, '1')

def oxygen_generator_rating(bin_nums):
    for i in range(len(bin_nums[0])):
        bit = check_bit_for_oxygen(bin_nums, i)
        bin_nums = list(keep_with_position_having_bit(bin_nums, i, bit))
        if len(bin_nums) == 1:
            return int(bin_nums[0], 2)

def check_bit_for_scrubber(bin_nums, position):
    bits = list(get_column_wise_list(bin_nums, position))
    return get_most_common_bit(bits, '0', True)

def co2_scrubber_rating(bin_nums):
    for i in range(len(bin_nums[0])):
        bit = check_bit_for_scrubber(bin_nums, i)
        bin_nums = list(keep_with_position_having_bit(bin_nums, i, bit))
        if len(bin_nums) == 1:
            return int(bin_nums[0], 2)

def main():
    bits = '''00100\n11110\n10110\n10111\n10101\n
    01111\n00111\n11100\n10000\n11001\n00010\n01010'''
    bits = bits.strip().split()
    n1 = oxygen_generator_rating(bits)
    n2 = co2_scrubber_rating(bits)
    print(n1, n2, n1 * n2)

    bin_nums = list(fcommands())
    n1 = oxygen_generator_rating(bin_nums)
    n2 = co2_scrubber_rating(bin_nums)
    print(n1, n2, n1 * n2)

if __name__ == '__main__':
    main()
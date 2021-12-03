from aoc_helpers import fcommands

def get_column_wise_list(a_list, col_no):
    for row in a_list:
        yield row[col_no]

def get_most_common_bit(a_list, succ_if_equal = None, invert = False):
    zeros = a_list.count('0')
    ones = a_list.count('1')
    if zeros == ones and succ_if_equal:
        return succ_if_equal
    result = '0' if zeros > ones else '1'
    if not invert:
        return result
    else:
        return '1' if result == '0' else '0'

def calculate_gamma_rate(bit_rows):
    binary_number = ''
    for nth_bit in range(len(bit_rows[0])):
        bits = list(get_column_wise_list(bit_rows, nth_bit))
        binary_number += get_most_common_bit(bits)
    return int(binary_number, 2)

def calculate_epsilon_rate(gamma_rate):
    return int(
        ''.join(
            '0' if b == '1' else '1'
            for b in bin(gamma_rate)[2:]
    ), 2)

def power_consumption(gamma_rate, epsilon_rate):
    return gamma_rate * epsilon_rate

def calculate(bit_rows):
    gamma_rate = calculate_gamma_rate(bit_rows)
    epsilon_rate = calculate_epsilon_rate(gamma_rate)
    return power_consumption(gamma_rate, epsilon_rate)

def main():
    bits = '''00100\n11110\n10110\n10111\n10101\n
    01111\n00111\n11100\n10000\n11001\n00010\n01010'''
    print(calculate(bits.strip().split()))

    print(calculate(list(fcommands())))

if __name__ == '__main__':
    main()
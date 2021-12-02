from aoc_helpers import (get_numbers_generator,
    get_current_input_file)

def count_depth_measurement_increases(messages):
    return list(messages.values()).count('(increased)')

def larger_than_previous_measurement(report, label = 'measurement'):
    previous = None
    messages = {
        0: '(N/A - no previous {})'.format(label),
    }
    for idx, measurement in enumerate(report):
        if idx in messages:
            print(measurement, messages[idx])
        elif previous != None:
            if previous == measurement:
                messages[idx] = '(no change)'
            if previous > measurement:
                messages[idx] = '(decreased)'
            elif previous < measurement:
                messages[idx] = '(increased)'
            print(measurement, messages[idx])
        previous = measurement
    return count_depth_measurement_increases(messages)

def main():
    # report = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    nums_gen = get_numbers_generator(get_current_input_file())
    print(larger_than_previous_measurement(nums_gen))

if __name__ == '__main__':
    main()
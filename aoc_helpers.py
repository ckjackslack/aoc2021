import os, sys

def get_current_name():
    return os.path.basename(os.path.splitext(sys.argv[0])[0])

def get_current_input_file():
    return f"{get_current_name().lstrip('_').split('_')[0]}_input.txt"

def get_lines(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()

def get_numbers_generator(filename):
    with open(filename) as f:
        for line in f:
            if line:
                yield int(line.strip())

def get_numbers_from_sliding_window(data, n = 3):
    yield from (
        cur
        for i
        in range(len(data))
        if len(cur := data[i:i+n]) == n
    )

def sum_sublists(main_list):
    return (sum(sublist) for sublist in main_list)

fcommands = lambda: get_lines(get_current_input_file())
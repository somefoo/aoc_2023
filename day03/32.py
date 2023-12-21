import numpy as np

with open("input.txt") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

    def run_to_find_end_of_digit(lines, x, y):
        while x < len(lines[y]) and lines[y][x] in '0123456789':
            x += 1
        return x

    def check_window_for_special_characters(lines, x_start, x_end, y_line):
        min_y = max(0, y_line-1)
        max_y = min(len(lines), y_line+2)
        min_x = max(0, x_start-1)
        max_x = min(len(lines[y_line]), x_end+1)
        for y in range(min_y, max_y):
            print(lines[y][min_x:max_x])
            for x in range(min_x, max_x):
                if lines[y][x] == '*':
                    return [y, x]
        return None

    valid_numbers_prod = np.ones((len(lines), len(lines[0])), dtype=int)
    valid_numbers_count = np.zeros((len(lines), len(lines[0])), dtype=int)

    valid_numbers = []
    y = 0
    while y < len(lines):
        x = 0
        while x < len(lines[y]):
            if lines[y][x] in '0123456789':
                x_end = run_to_find_end_of_digit(lines, x, y)
                #print(y,x)
                print(lines[y][x:x_end])
                pos = check_window_for_special_characters(lines, x, x_end, y)
                if pos is not None:
                    valid_numbers_prod[pos[0], pos[1]] *= int(lines[y][x:x_end])
                    valid_numbers_count[pos[0], pos[1]] += 1
                x = x_end
            x += 1
        y += 1

        valid_numbers_count_mask = (valid_numbers_count == 2)
        print(valid_numbers_prod * valid_numbers_count_mask)
        print(np.sum(valid_numbers_prod * valid_numbers_count_mask))

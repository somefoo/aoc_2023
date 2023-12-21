with open("input.txt") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

    lines = [line.split(" ") for line in lines]
    lines = [[int(x) for x in line] for line in lines]


    def get_difference(line):
        new_line = []
        for i in range(1, len(line)):
            new_line.append(line[i] - line[i - 1])

        return new_line

    def get_difference_until_all_zero(line):
        new_lines = [line, get_difference(line)]
        while not all([x == 0 for x in new_lines[-1]]):
            new_lines.append(get_difference(new_lines[-1]))

        return new_lines

    extrapolation_values = []
    preextrapolation_values = []

    for line in lines:
        new_lines = get_difference_until_all_zero(line)
        sum_of_last = sum(line[-1] for line in new_lines)
        extrapolation_values.append(sum_of_last)

        new_lines = new_lines[::-1]
        new_lines[0].insert(0, 0)

        for i in range(1, len(new_lines)):
            new_values = new_lines[i][0] - new_lines[i - 1][0]
            new_lines[i].insert(0,new_lines[i][0] - new_lines[i - 1][0])

        new_lines = new_lines[::-1]
        preextrapolation_values.append(new_lines[0][0])


    print(sum(extrapolation_values))
    print(sum(preextrapolation_values))

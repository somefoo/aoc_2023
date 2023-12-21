with open('input.txt') as f:
    lines = f.readlines()

    sum = 0
    for line in lines:
        line = [int(x) for x in line if x in '0123456789']
        sum += line[0]*10 + line[-1]

    print(sum)

with open('input2.txt') as f:
    lines = f.readlines()

    def replace_words(line):
        line_list = []
        # Find first number
        line_list.append(line.replace('one', '1', 1))
        line_list.append(line.replace('two', '2', 1))
        line_list.append(line.replace('three', '3', 1))
        line_list.append(line.replace('four', '4', 1))
        line_list.append(line.replace('five', '5', 1))
        line_list.append(line.replace('six', '6', 1))
        line_list.append(line.replace('seven', '7', 1))
        line_list.append(line.replace('eight', '8', 1))
        line_list.append(line.replace('nine', '9', 1))
        line_list.append(line.replace('zero', '0', 1))

        def find_first_number(line):
            for i in range(len(line)):
                if line[i] in '0123456789':
                    return i
            return -1

        most_front_line = line
        for line in line_list:
            if find_first_number(line) < find_first_number(most_front_line):
                most_front_line = line

        return most_front_line

    def replace_words_backwards(line):
        line = line[::-1]
        line_list = []
        # Find first number
        line_list.append(line.replace('eno', '1', 1))
        line_list.append(line.replace('owt', '2', 1))
        line_list.append(line.replace('eerht', '3', 1))
        line_list.append(line.replace('ruof', '4', 1))
        line_list.append(line.replace('evif', '5', 1))
        line_list.append(line.replace('xis', '6', 1))
        line_list.append(line.replace('neves', '7', 1))
        line_list.append(line.replace('thgie', '8', 1))
        line_list.append(line.replace('enin', '9', 1))
        line_list.append(line.replace('orez', '0', 1))

        def find_first_number(line):
            for i in range(len(line)):
                if line[i] in '0123456789':
                    return i
            return -1

        most_front_line = line
        for line in line_list:
            if find_first_number(line) < find_first_number(most_front_line):
                most_front_line = line

        return most_front_line[::-1]

    sum = 0
    for line in lines:
        line = replace_words(line)
        line = replace_words_backwards(line)
        line = [int(x) for x in line if x in '0123456789']
        sum += line[0]*10 + line[-1]

    print(sum)




def irange(start, end, step=1):
    mins = min(start, end)
    maxs = max(start, end)
    return range(int(mins), int(maxs)+1, step)

with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

    lines = [line.split(" ") for line in lines]

    typed_lines = []

    for line in lines:
        length = int(line[1])
        color = int(line[2][2:-1], 16)

        d = line[0]
        direction = (d == "R") * (1 + 0j) + (d == "L") * (-1 + 0j) + (d == "U") * (0 - 1j) + (d == "D") * (0 + 1j)

        typed_lines.append((direction, length, color))
        #print(direction*length, length, color)

    compute_size = sum([line[0]*line[1] for line in typed_lines])

    max_x = -10000000
    max_y = -10000000
    min_x = 10000000
    min_y = 10000000
    position = 0 + 0j
    for line in typed_lines:
        position += line[0]*line[1]
        max_x = max(max_x, position.real)
        max_y = max(max_y, position.imag)
        min_x = min(min_x, position.real)
        min_y = min(min_y, position.imag)

    dig_map = {x + y*1j:'.' for x in range(int(min_x), int(max_x+1)) for y in range(int(min_y), int(max_y+1))}

    position = 0 + 0j
    for line in typed_lines:
        for x in irange(position.real, position.real + line[0].real*line[1]):
            for y in irange(position.imag, position.imag + line[0].imag*line[1]):
                dig_map[x + y*1j] = '#'
        position += line[0]*line[1]


    for y in range(int(min_y), int(max_y+1)):
        for x in range(int(min_x), int(max_x+1)):
            print(dig_map[x + y*1j], end='')

        print()
    print()


    assert position == 0 + 0j

    for y in range(int(min_y), int(max_y)):
        inside = False
        x = min_x
        while x < max_x:
            if dig_map[x + y*1j] == '#':
                v = '.'

                #if pos + 1j in dig_map and dig_map[pos + 1j] == '#' and pos - 1j in dig_map and dig_map[pos - 1j] == '#':

                above = x + y*1j - 1j
                below = x + y*1j + 1j
                while x + y*1j in dig_map and dig_map[x + y*1j] == '#':
                    x += 1
                new_above = x-1 + y*1j - 1j
                new_below = x-1 + y*1j + 1j


                if above in dig_map and below in dig_map and dig_map[above] == '#' and dig_map[below] == '#':
                    inside = not inside
                    #dig_map[x + y*1j] = (inside)*1
                    #v = str((inside)*1)
                    #v = 'X'
                elif above in dig_map and new_above in dig_map and dig_map[above] !=  dig_map[new_above]:
                    inside = not inside
                    #dig_map[x + y*1j] = (inside)*2
                    #v = str((inside)*2)
                    #v = 'X'
                elif below in dig_map and new_below in dig_map and dig_map[below] !=  dig_map[new_below]:
                    inside = not inside
                    #dig_map[x + y*1j] = (inside)*3
                    #v = str((inside)*3)
                    #v = 'X'
                if inside:
                    v = 'X'
                else:
                    v = '.'

            if inside:
                dig_map[x + y*1j] = v
            x += 1


    count = 0
    for y in range(int(min_y), int(max_y+1)):
        for x in range(int(min_x), int(max_x+1)):
            print(dig_map[x + y*1j], end='')
            if dig_map[x + y*1j] == '#' or dig_map[x + y*1j] == 'X':
                count += 1
        print()

    print("A:", count)

    #for line in lines:
    #    print(line)

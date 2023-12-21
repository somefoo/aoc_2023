with open('input.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

    width = len(lines[0])
    height = len(lines)


    print(width, height)

    map = [[-1 for col in range(width)] for row in range(height)]
    lr_map = [['N' for col in range(width)] for row in range(height)]


    def print_map():
        print("#############")
        for y in range(height):
            for x in range(width):
                if map[y][x] == -1:
                    print('.', end='\t')
                else:
                    print(map[y][x], end='\t')
            print()

        print("-----------")

        for y in range(height):
            for x in range(width):
                print(lines[y][x], end='')
            print()

        print("-----------")

        for y in range(height):
            for x in range(width):
                print(lr_map[y][x], end='')
            print()
        print("#############")


    stack = []

    for y in range(height):
        for x in range(width):
            if lines[y][x] == 'S':
                print('S', x, y)
                stack.append((x, y))
                map[y][x] = 0

    assert len(stack) == 1

    while len(stack) > 0:
        x, y = stack.pop()
        print(x, y)
        #if x == 3 and y == 1:
        #    print('FOUND IT')
        #    print(lines[y][x])
        #    breakpoint()
        if not (x >= 0 and y >= 0 and x <= width - 1 and y <= height - 1):
            continue

        going_west =  ['S','-', 'J', '7']
        going_east =  ['S','-', 'L', 'F']
        going_south = ['S','|', '7', 'F']
        going_north = ['S','|', 'L', 'J']

        coming_from_east =  ['-', 'L', 'F']
        coming_from_west =  ['-', 'J', '7']
        coming_from_north = ['|', 'L', 'J']
        coming_from_south = ['|', '7', 'F']

        if x+1 < width and map[y][x + 1] == -1 and lines[y][x] in going_east and lines[y][x + 1] in coming_from_west:
            map[y][x + 1] = map[y][x] + 1
            stack.insert(0, (x + 1, y))

            if y+1 < height:
                lr_map[y+1][x] = 'L'
                lr_map[y+1][x+1] = 'L'
            if y-1 >= 0:
                lr_map[y-1][x] = 'R'
                lr_map[y-1][x+1] = 'R'

        elif x-1 >= 0 and map[y][x - 1] == -1 and lines[y][x] in going_west and lines[y][x - 1] in coming_from_east:
            map[y][x - 1] = map[y][x] + 1
            stack.insert(0, (x - 1, y))

            if y+1 < height:
                lr_map[y+1][x] = 'R'
                lr_map[y+1][x-1] = 'R'
            if y-1 >= 0:
                lr_map[y-1][x] = 'L'
                lr_map[y-1][x-1] = 'L'

        elif y+1 < height and map[y + 1][x] == -1 and lines[y][x] in going_south and lines[y + 1][x] in coming_from_north:
            map[y + 1][x] = map[y][x] + 1
            stack.insert(0, (x, y + 1))

            if x+1 < width:
                lr_map[y][x+1] = 'R'
                lr_map[y+1][x+1] = 'R'
            if x-1 >= 0:
                lr_map[y][x-1] = 'L'
                lr_map[y+1][x-1] = 'L'

        elif y-1 >= 0 and map[y - 1][x] == -1 and lines[y][x] in going_north and lines[y - 1][x] in coming_from_south:
            map[y - 1][x] = map[y][x] + 1
            stack.insert(0 ,(x, y - 1))

            if x+1 < width:
                lr_map[y][x+1] = 'L'
                lr_map[y-1][x+1] = 'L'
            if x-1 >= 0:
                lr_map[y][x-1] = 'R'
                lr_map[y-1][x-1] = 'R'

        #print_map()

        #if lines[y][x] == 'S':
        #    false_direction = stack.pop()


    print(max([max(row) for row in map]))


    for y in range(height):
        for x in range(width):
            if map[y][x] >= 0:
                #lr_map[y][x] = lines[y][x]
                lr_map[y][x] = '#'


    while True:
        changed = 0
        for y in range(height):
            for x in range(width):
                if lr_map[y][x] == 'N':
                    # Check neighbors for L or R
                    if x+1 < width and lr_map[y][x+1] in ['L', 'R']:
                        lr_map[y][x] = lr_map[y][x+1]
                        changed += 1
                    elif x-1 >= 0 and lr_map[y][x-1] in ['L', 'R']:
                        lr_map[y][x] = lr_map[y][x-1]
                        changed += 1
                    elif y+1 < height and lr_map[y+1][x] in ['L', 'R']:
                        lr_map[y][x] = lr_map[y+1][x]
                        changed += 1
                    elif y-1 >= 0 and lr_map[y-1][x] in ['L', 'R']:
                        lr_map[y][x] = lr_map[y-1][x]
                        changed += 1
        if changed == 0:
            break

    print_map()

    # Go along edges and find the letters
    l_outside_counter = 0

    for x in range(width):
        if lr_map[0][x] == 'L':
            l_outside_counter += 1
        if lr_map[height-1][x] == 'L':
            l_outside_counter += 1
    for y in range(height):
        if lr_map[y][0] == 'L':
            l_outside_counter += 1
        if lr_map[y][width-1] == 'L':
            l_outside_counter += 1

    inside = 'L'
    if l_outside_counter > 0:
        inside = 'R'

    # Count number of inside letters
    print(len([1 for y in range(height) for x in range(width) if lr_map[y][x] == inside]))

    # Print number of characters that are not in 'N,#,L,R'
    print(len([1 for y in range(height) for x in range(width) if lr_map[y][x] == 'N']))



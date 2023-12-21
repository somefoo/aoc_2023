with open('input.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

    width = len(lines[0])
    height = len(lines)


    print(width, height)

    map = [[-1 for col in range(width)] for row in range(height)]


    def print_map():
        print("#############")
        for y in range(height):
            for x in range(width):
                if map[y][x] == -1:
                    print('.', end='')
                else:
                    print(map[y][x], end='')
            print()

        print("-----------")

        for y in range(height):
            for x in range(width):
                print(lines[y][x], end='')
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
        if x-1 >= 0 and map[y][x - 1] == -1 and lines[y][x] in going_west and lines[y][x - 1] in coming_from_east:
            map[y][x - 1] = map[y][x] + 1
            stack.insert(0, (x - 1, y))
        if y+1 < height and map[y + 1][x] == -1 and lines[y][x] in going_south and lines[y + 1][x] in coming_from_north:
            map[y + 1][x] = map[y][x] + 1
            stack.insert(0, (x, y + 1))
        if y-1 >= 0 and map[y - 1][x] == -1 and lines[y][x] in going_north and lines[y - 1][x] in coming_from_south:
            map[y - 1][x] = map[y][x] + 1
            stack.insert(0 ,(x, y - 1))


        #print_map()

    print(max([max(row) for row in map]))

    print_map()



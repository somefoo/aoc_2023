with open('input.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

    grid = [['.' for _ in range(len(lines[0]))] for _ in range(len(lines))]

    def setGrid(x,y,char):
        if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
            return False
        if grid[y][x] == char:
            return False
        grid[y][x] = char
        return True

    def getLineChar(x,y):
        if x < 0 or x >= len(lines[0]) or y < 0 or y >= len(lines):
            return None
        return lines[y][x]

    beams = [((0,0), (1,0))]

    def reflect(beam, char, width, height):
        x,y = beam[0]
        dx,dy = beam[1]

        if x < 0 or x >= width or y < 0 or y >= height:
            return []

        if char == '.':
            return [((x+dx, y+dy), (dx,dy))]
        elif char == '/':
            if dx == 0:
                return [((x-dy, y), (-dy,dx))]
            else:
                return [((x, y-dx), (dy,-dx))]
        elif char == '\\':
            if dx == 0:
                return [((x+dy, y), (dy,dx))]
            else:
                return [((x, y+dx), (dy,dx))]
        elif char == '|':
            if dx != 0:
                return [((x, y+1), (0,1)), ((x, y-1), (0,-1))]
            else:
                return [((x+dx, y+dy), (dx,dy))]
        elif char == '-':
            if dy != 0:
                return [((x+1, y), (1,0)), ((x-1, y), (-1,0))]
            else:
                return [((x+dx, y+dy), (dx,dy))]


    for line in lines:
        print(line)



    while len(beams) > 0:
#    for i in range(len(lines)*len(lines[0])*500):
        beam = beams.pop(0)

        beam_direction = beam[1]
        char = '^'
        if beam_direction == (1,0):
            char = '>'
        elif beam_direction == (-1,0):
            char = '<'
        elif beam_direction == (0,-1):
            char = 'v'
        elif beam_direction == (0,1):
            char = '^'
        else:
            print("ERROR")


        #print(beam)
        #print(len(grid[0]), len(grid))
        line_char = getLineChar(beam[0][0], beam[0][1])

        if line_char == None:
            continue

        if setGrid(beam[0][0], beam[0][1], char):
            beams += reflect(beam, line_char, len(lines[0]), len(lines))
        #for g in grid:
        #    print(g)
        #print()
        #from time import sleep
#        sleep(0.3)

    for g in grid:
        print(g)

    count = 0
    for g in grid:
        for c in g:
            if c != '.':
                count += 1
    print(count)



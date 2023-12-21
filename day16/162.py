with open('input.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    #grid = [['.' for _ in range(len(lines[0]))] for _ in range(len(lines))]


    def setGrid(x,y,char,grid):
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



    def compute_energy(starting_beam):
        grid = [['.' for _ in range(len(lines[0]))] for _ in range(len(lines))]
        beams = [starting_beam]
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

            if setGrid(beam[0][0], beam[0][1], char, grid):
                beams += reflect(beam, line_char, len(lines[0]), len(lines))
            #for g in grid:
            #    print(g)
            #print()
            #from time import sleep
#        sleep(0.3)

        #for g in grid:
        #    print(g)

        count = 0
        for g in grid:
            for c in g:
                if c != '.':
                    count += 1
        print(count)
        return count

    top_starting_beams = [((x,0), (0,1)) for x in range(len(lines[0]))]
    bottom_starting_beams = [((x,len(lines)-1), (0,1)) for x in range(len(lines[0]))]
    left_starting_beams = [((0,y), (1,0)) for y in range(len(lines))]
    right_starting_beams = [((len(lines[0])-1,y), (-1,0)) for y in range(len(lines))]
    starting_beams = top_starting_beams + bottom_starting_beams + left_starting_beams + right_starting_beams

    max_energy = 0
    for beam in starting_beams:
        energy = compute_energy(beam)
        if energy > max_energy:
            max_energy = energy
        print(beam, energy)

    print("Max energy:", max_energy)
    #energies = [compute_energy(beam) for beam in starting_beams]
    #print(max(energies))
    #compute_energy(((0,0), (1,0)))

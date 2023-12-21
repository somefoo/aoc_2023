with open('input.txt') as f:
    grid_map = f.readlines()
    grid_map = [line.strip().split()[-1] for line in grid_map]

    directions = {'0': (1,0), '1': (0,1), '2': (-1,0), '3': (0,-1)}
    grid_map = [(directions[hexv[7]], int(hexv[2:7], 16)) for hexv in grid_map]

    x_position = 0
    volume = 0
    for (x,y), n in grid_map:
        x_position += x*n
        volume += y*n * x_position
        volume += n/2
    print(int(volume + 1))


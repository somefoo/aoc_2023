with open('input.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]



    def enlarge_rows(lines):
        lines_enlarged = []
        for line in lines:
            if "#" in line:
                lines_enlarged.append(line)
            else:
                lines_enlarged.append(line)
                lines_enlarged.append(line)
        return lines_enlarged

    def transpose(l):
        return [list(i) for i in zip(*l)]

    lines = enlarge_rows(lines)
    lines = transpose(lines)
    lines = enlarge_rows(lines)
    lines = transpose(lines)

    counter = 0
    for line in lines:
        for i in range(0, len(line)):
            if line[i] == '#':
                line[i] = counter
                counter += 1

    shortest_paths_found = set()
    shortest_paths_list = []

    for line in lines:
        print(line)


    for i in range(0, counter):
        map = [line.copy() for line in lines]
        front = []

        for x in range(0, len(lines[0])):
            for y in range(0, len(lines)):
                if map[y][x] == i:
                    front.append((x + 1, y))
                    front.append((x - 1, y))
                    front.append((x, y + 1))
                    front.append((x, y - 1))

        next_front = []
        wave = 1
        while True:
            while front != []:
                element = front.pop(0)
                x = element[0]
                y = element[1]
                if x < 0 or y < 0 or x >= len(map[0]) or y >= len(map):
                    continue
                if map[y][x] == '#':
                    continue
                elif map[y][x] != '.' and map[y][x] != i:
                    min_val = min(i, map[y][x])
                    max_val = max(i, map[y][x])

                    if (min_val, max_val) in shortest_paths_found:
                        continue
                    else:
                        shortest_paths_found.add((min_val, max_val))
                        shortest_paths_list.append((min(i, map[y][x]), max(i, map[y][x]), wave))

                next_front.append((x + 1, y))
                next_front.append((x - 1, y))
                next_front.append((x, y + 1))
                next_front.append((x, y - 1))
                map[y][x] = '#'
            wave += 1

            if next_front == []:
                break
            front = next_front
            next_front = []

    # Sum of all shortest paths
    sum = 0
    for path in shortest_paths_list:
        sum += path[2]

    print(sum)


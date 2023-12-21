# Comment to self, next time think more... The problem was easy with manhatten distance

with open('input.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

    def enlarge_rows(lines):
        lines_enlarged = []
        for line in lines:
            if "#" in line:
                lines_enlarged.append(line)
            else:
                # Replace all '.' with '+' in line
                line = ['+' if x == '.' else x for x in line]
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
    shortest_path_dict = {}

    for line in lines:
        print(line)


    for i in range(0, counter):
        map = [line.copy() for line in lines]
        front = []

        for x in range(0, len(lines[0])):
            for y in range(0, len(lines)):
                if map[y][x] == i:
                    front.append((x, y,0))

        next_front = []
        wave = 0
        while True:
            while front != []:
                element = front.pop(0)
                x = element[0]
                y = element[1]
                star_counter = element[2]
                if x < 0 or y < 0 or x >= len(map[0]) or y >= len(map):
                    continue
                if map[y][x] == '#':
                    continue
                elif map[y][x] == '+':
                    star_counter += 1000000
                elif map[y][x] == '.':
                    star_counter += 1
                elif map[y][x] != '.' and map[y][x] != i:
                    star_counter += 1
                    min_val = min(i, map[y][x])
                    max_val = max(i, map[y][x])

                    #shortest_path_dict[(min_val, max_val)] = min(wave+1000000*star_counter, shortest_path_dict.get((min_val, max_val), 100000000000000000))
                    shortest_path_dict[(min_val, max_val)] = min(star_counter, shortest_path_dict.get((min_val, max_val), 100000000000000000))

                next_front.append((x + 1, y, star_counter))
                next_front.append((x - 1, y, star_counter))
                next_front.append((x, y + 1, star_counter))
                next_front.append((x, y - 1, star_counter))
                map[y][x] = '#'
            wave += 1

            if next_front == []:
                break
            front = next_front
            next_front = []
    sum = 0
    for key in shortest_path_dict:
        sum += shortest_path_dict[key]
    print(sum)

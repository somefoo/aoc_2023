from math import lcm

with open('input.txt') as f:
    data = f.read().splitlines()

    directions = data[0]

    data = data[2:]

    # Remove all special characters (sometimes with space)
    data = [x.replace('(', '').replace(')', '').replace('= ', '').replace(',','') for x in data]

    starting_nodes = []
    graph = {}
    for line in data:
        line = line.split()
        if line[0][2] == 'A':
            starting_nodes.append(line[0])
        graph[line[0]] = line[1:]



    z_loop_size = []

    for n in range(len(starting_nodes)):
        last_seen_z = 0
        i = 0
        while True:
            current_node = starting_nodes[n]
            neighbours = graph[current_node]
            action = directions[i % len(directions)]
            if action == 'L':
                starting_nodes[n] = neighbours[0]
            elif action == 'R':
                starting_nodes[n] = neighbours[1]
            i += 1

            if starting_nodes[n][-1] == 'Z':
                z_loop_size.append(i - last_seen_z)
                last_seen_z = i
                break

    print(z_loop_size)
    print(lcm(*z_loop_size))

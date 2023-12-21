with open('input.txt') as f:
    data = f.read().splitlines()

    directions = data[0]

    data = data[2:]

    # Remove all special characters (sometimes with space)
    data = [x.replace('(', '').replace(')', '').replace('= ', '').replace(',','') for x in data]

    graph = {}
    for line in data:
        line = line.split()
        graph[line[0]] = line[1:]


    current_node = 'AAA'
    i = 0
    while current_node != 'ZZZ':
        neighbours = graph[current_node]
        action = directions[i % len(directions)]
        if action == 'L':
            current_node = neighbours[0]
        elif action == 'R':
            current_node = neighbours[1]

        print(current_node)

        i += 1
    print(graph)

    print(i)

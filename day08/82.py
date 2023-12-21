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


    #print(starting_nodes)

    #current_node = 'AAA'
    i = 0
    while True:
        #print(starting_nodes)
        for n in range(len(starting_nodes)):
            current_node = starting_nodes[n]
            neighbours = graph[current_node]
            action = directions[i % len(directions)]
            if action == 'L':
                starting_nodes[n] = neighbours[0]
            elif action == 'R':
                starting_nodes[n] = neighbours[1]
        i += 1

        # Print number of current nodes with 'Z' at the end
        a = sum([x[-1] == 'Z' for x in starting_nodes])
        if a > 1:
            print(starting_nodes, a)

        # Check if all starting nodes end with 'Z'
        if all([x[-1] == 'Z' for x in starting_nodes]):
            break

        if i % 10000 ==0:
            print(i)

    print(i)

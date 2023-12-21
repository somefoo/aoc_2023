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

    round_trips = [[] for x in range(len(starting_nodes))]

    current_nodes = starting_nodes.copy()


    for n in range(len(current_nodes)):
        while True:
            current_node = current_nodes[n]
            round_trips[n].append(current_node)

            neighbours = graph[current_node]
            action = directions[0]
            if action == 'L':
                current_nodes[n] = neighbours[0]
            elif action == 'R':
                current_nodes[n] = neighbours[1]

            if current_nodes[n] in round_trips[n]:
                print("found loop")
                round_trips[n].append(current_nodes[n])
                break


    for round_trip in round_trips:
        print("#####")
        print(len(round_trip))
        print(round_trip)
        print("#####")
    exit()

    #current_node = 'AAA'
    i = 0
    while True:
        #print(current_nodes)
        for n in range(len(current_nodes)):
            current_node = current_nodes[n]

            round_trips[n].append(current_node)

            neighbours = graph[current_node]
            action = directions[i % len(directions)]
            if action == 'L':
                current_nodes[n] = neighbours[0]
            elif action == 'R':
                current_nodes[n] = neighbours[1]
        i += 1
        # Check if all starting nodes end with 'Z'
        if all([x[-1] == 'Z' for x in current_nodes]):
            break

    print(round_trips)

    print(i)

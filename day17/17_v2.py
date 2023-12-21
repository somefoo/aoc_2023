from queue import PriorityQueue

with open('input2.txt') as f:
    data = f.readlines()
    data = [x.strip() for x in data]
    data = [list(x) for x in data]
    data = [[int(y) for y in x] for x in data]

    data_visited = [[9999 for _ in range(len(data[0]))] for y in range(len(data))]
    shortest_path = [[9999 for _ in range(len(data[0]))] for y in range(len(data))]
    path_path = [['.' for _ in range(len(data[0]))] for y in range(len(data))]

    width = len(data[0])
    height = len(data)

    get_node = lambda x,y: [data[y][x],x,y,0,0,'.']

    def get_neighbours(node):
        w,x,y,x_count,y_count = node[0],node[1],node[2],node[3],node[4]
        neighbours = []
        max_line_jump = 3

        if x_count == 0:
            jump_cost = w
            for i in range(min(x+1, width), min(x+4,width)):
                node = get_node(i,y)
                node[0] += jump_cost
                jump_cost += node[0] - jump_cost
                node[3] = x_count + i-x
                if node[3] > max_line_jump:
                    break
                node[5] = '>'
                neighbours.append(node)

            jump_cost = w

            for i in range(max(0, x-1), max(-1,x-4), -1):
                node = get_node(i,y)
                node[0] += jump_cost
                jump_cost += x_count + node[0] - jump_cost
                node[3] += x-i
                if node[3] > max_line_jump:
                    break
                node[5] = '<'
                neighbours.append(node)

        if y_count == 0:
            jump_cost = w

            for j in range(min(y+1, height), min(y+4,height)):
                node = get_node(x,j)
                node[0] += jump_cost
                jump_cost += node[0] - jump_cost
                node[4] += y_count + j-y
                if node[4] > max_line_jump:
                    break
                node[5] = 'v'
                neighbours.append(node)

            jump_cost = w

            for j in range(max(0, y-1), max(-1,y-4), -1):
                node = get_node(x,j)
                node[0] += jump_cost
                jump_cost += node[0] - jump_cost
                node[4] += y_count + y-j
                if node[4] > max_line_jump:
                    break
                node[5] = '^'
                neighbours.append(node)

        return neighbours



#    stack = [get_node(0,0)]

    queue = PriorityQueue()
    queue.put(get_node(0,0))

    #if True:
    #    n = get_neighbours(get_node(3,3))
    #    for node in n:
    #        print(node[1], node[2])
    #    print(len(n))
    #exit()

    while not queue.empty():
        node = queue.get()
        #print(node)

        if data_visited[node[2]][node[1]] <= node[0]:
            continue
        data_visited[node[2]][node[1]] = node[0]

        shortest_path[node[2]][node[1]] = min(node[0], shortest_path[node[2]][node[1]])
        path_path[node[2]][node[1]] = node[5]

        if node[1] == width-1 and node[2] == height-1:
            print(node)
#            break



        for neighbour in get_neighbours(node):
            queue.put(neighbour)



    #for line in shortest_path:
    #    for node in line:
    #        print('\t' + str(node), end='')
    #    print()

    #for line in path_path:
    #    for node in line:
    #        print('\t' + str(node), end='')
    #    print()

    last_node = [width-1, height-1]
    path = []
    while last_node != [0,0]:
        path.append(path_path[last_node[1]][last_node[0]])
        data[last_node[1]][last_node[0]] = path[-1]
        if path[-1] == '>':
            last_node[0] -= 1
        elif path[-1] == '<':
            last_node[0] += 1
        elif path[-1] == 'v':
            last_node[1] -= 1
        elif path[-1] == '^':
            last_node[1] += 1


    path.reverse()
    #print(path)

    for line in data:
        for node in line:
            print('' + str(node), end='')
        print()

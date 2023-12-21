from queue import PriorityQueue

with open('input.txt') as f:
    data = f.readlines()
    data = [x.strip() for x in data]
    data = [list(x) for x in data]
    data = [[int(y) for y in x] for x in data]

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
                if (x,y) == (i,y): continue
                node = get_node(i,y)
                node[0] += jump_cost
                jump_cost = node[0]
                node[3] = 1
                neighbours.append(node)

            jump_cost = w

            for i in range(max(0, x-1), max(-1,x-4), -1):
                if (x,y) == (i,y): continue
                node = get_node(i,y)
                node[0] += jump_cost
                jump_cost = node[0]
                node[3] = -1
                neighbours.append(node)

        if y_count == 0:
            jump_cost = w

            for j in range(min(y+1, height), min(y+4,height)):
                if (x,y) == (x,j): continue
                node = get_node(x,j)
                node[0] += jump_cost
                jump_cost = node[0]
                node[4] = 1
                neighbours.append(node)

            jump_cost = w

            for j in range(max(0, y-1), max(-1,y-4), -1):
                if (x,y) == (x,j): continue
                node = get_node(x,j)
                node[0] += jump_cost
                jump_cost = node[0]
                node[4] = -1
                neighbours.append(node)

        return neighbours



#    stack = [get_node(0,0)]

    queue = PriorityQueue()
    #queue.put(get_node(0,0))
    #queue.put(get_node(0,1))
    queue.put(get_node(0,0))

    #if True:
    #    n = get_neighbours(get_node(3,3))
    #    for node in n:
    #        print(node)
    #    print(len(n))
    #exit()

    seen = set()

    while not queue.empty():
        node = queue.get()
        print(node)

        if node[1] == width-1 and node[2] == height-1:
            print(node)
            print(node[0] - data[0][0])
            break

        if (node[1],node[2],node[3],node[4]) in seen:
            continue

        seen.add((node[1],node[2],node[3],node[4]))


        for neighbour in get_neighbours(node):
            queue.put(neighbour)

    print("DONE")




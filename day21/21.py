with open('input.txt') as f:
    lines = [line.strip() for line in f]
    #lines = {x + y*1j:c for y, line in enumerate(lines) for x, c in enumerate(line)} 
    lines = {x + y*1j:(-1 if c == '.' else c) for y, line in enumerate(lines) for x, c in enumerate(line)} 

    start = next(k for k, v in lines.items() if v == 'S')


    lines[start] = 0
    front = [start]
    even_counter = 1 # Include 0

    for counter in range(1,64+1):
        new_front = [] 
        for pos in front:
            for d in [1, -1, 1j, -1j]:
                if pos + d not in lines:
                    continue
                if lines[pos + d] == -1:
                    lines[pos + d] = counter
                    new_front.append(pos + d)
        if counter % 2 == 0:
            even_counter += len(new_front)
        front = new_front

    print(even_counter)
    exit()

    for i in range(0,max(int(x.real) for x in lines.keys())+1):
        for j in range(0,max(int(x.imag) for x in lines.keys())+1):
            if i + j*1j in lines:
                print(str(lines[i + j*1j]).zfill(2), end=' ')
        print("")





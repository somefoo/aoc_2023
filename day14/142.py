with open('input.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    lines = [list(x) for x in lines]

    #for cycle in range(4)
    def slide_up(lines_s):
        for i in range(1, len(lines_s)):
            for j in range(len(lines_s[i])):
                if lines_s[i][j] == 'O':
                    for k in range(1, i+1):
                        if lines_s[i-k][j] == '.':
                            lines_s[i-k][j] = 'O'
                            lines_s[i-k+1][j] = '.'
                        else:
                            break
    def slide_left(lines_s):
        for j in range(1, len(lines_s[0])):
            for i in range(len(lines_s)):
                if lines_s[i][j] == 'O':
                    for k in range(1, j+1):
                        if lines_s[i][j-k] == '.':
                            lines_s[i][j-k] = 'O'
                            lines_s[i][j-k+1] = '.'
                        else:
                            break
    def slide_down(lines_s):
        for i in range(len(lines_s)-2, -1, -1):
            for j in range(len(lines_s[i])):
                if lines_s[i][j] == 'O':
                    for k in range(1, len(lines_s)-i):
                        if lines_s[i+k][j] == '.':
                            lines_s[i+k][j] = 'O'
                            lines_s[i+k-1][j] = '.'
                        else:
                            break
    def slide_right(lines_s):
        for j in range(len(lines_s[0])-2, -1, -1):
            for i in range(len(lines_s)):
                if lines_s[i][j] == 'O':
                    for k in range(1, len(lines_s[0])-j):
                        if lines_s[i][j+k] == '.':
                            lines_s[i][j+k] = 'O'
                            lines_s[i][j+k-1] = '.'
                        else:
                            break

    hash_history = {}

    i = 0
    while i < 1000000000:
        # Get hash for lines
        list_of_hashes = []
        for line in lines:
            list_of_hashes.append(hash(''.join(line)))
        hash_of_lines = hash(tuple(list_of_hashes))
        print(hash_of_lines)
        
        if hash_of_lines in hash_history:
            print('Found cycle')
            print('current i: ', i)
            print('previous i: ', hash_history[hash_of_lines])
            difference = i - hash_history[hash_of_lines]
            # i + x * difference = 1000000000
            # x = (1000000000 - i) / difference
            multiplier = (1000000000 - i) // difference
            i += multiplier * difference

        hash_history[hash_of_lines] = i



        print(i / 1000000000, end='\r')
        slide_up(lines)
        slide_left(lines)
        slide_down(lines)
        slide_right(lines)


        for k in range(len(lines)):
            print(''.join(lines[k]))

        print('##########')
        print('          ')

        i += 1


    height = len(lines)
    sum = 0
    for i in range(height):
        sum += lines[i].count('O') * (height - i)

    print(sum)


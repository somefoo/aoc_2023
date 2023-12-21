with open('input.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    lines = [list(x) for x in lines]


    for i in range(1, len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == 'O':
                for k in range(1, i+1):
                    if lines[i-k][j] == '.':
                        lines[i-k][j] = 'O'
                        lines[i-k+1][j] = '.'
                    else:
                        break


    height = len(lines)
    sum = 0
    for i in range(height):
        sum += lines[i].count('O') * (height - i)

    print(sum)


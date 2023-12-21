with open('input.txt') as f:
    data = f.readlines()
    data = [x.strip() for x in data] + ['']

    #print(data)

    current = []

    def find_mirror_all(lines):
        list_of_mirrors = []
        for i in range(1, len(lines[0])):
            mirror_list = [line[0:i].endswith(line[i:][::-1]) for line in lines]
            if all(mirror_list):
                list_of_mirrors.append(i)

        lines_mirrored = [line[::-1] for line in lines]
        for i in range(len(lines[0])):
            mirror_list = [line[0:i].endswith(line[i:][::-1]) for line in lines_mirrored]
            if all(mirror_list):
                list_of_mirrors.append(len(lines[0]) - i)
        return list_of_mirrors

    sumall = 0

    for i in range(len(data)):
        if data[i] != '':
            current.append(data[i])
        if data[i] == '':
            current_transposed = [''.join(l) for l in list(map(list, zip(*current)))]

            print(find_mirror_all(current), find_mirror_all(current_transposed))

            sumall += sum(find_mirror_all(current))
            sumall += sum(find_mirror_all(current_transposed))*100

            current = []

    print(sumall)


with open('input.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

    map = [[] for i in range(256)]
    
    line = lines[0]
    words = line.split(',')


    current_value = 0

    def get_hash(w):
        word_sum = 0
        for char in word:
            word_sum += ord(char)
            word_sum *= 17
            word_sum %= 256
        return word_sum



    for word_whole in words:

        if word_whole[-1] == '-':
            word = word_whole[:-1]
            word_sum = get_hash(word)
            if map[word_sum] != []:
                index = -2
                # Go over map and remove the entry with the same word
                for i in range(len(map[word_sum])):
                    if map[word_sum][i].split('=')[0] == word:
                        index = i
                if index != -2:
                    map[word_sum].pop(index)
        else:
            word, value = word_whole.split('=')
            word_sum = get_hash(word)
            for i in range(len(map[word_sum])):
                if map[word_sum][i].split('=')[0] == word:
                    map[word_sum][i] = word_whole
                    break
            else:
                map[word_sum].append(word_whole)

        #print('Word: ', word_whole)
        #for i in range(0, 256):
        #    if map[i] != []:
        #        print(i, map[i])
        #print('------------------')
            
        #current_value += word_sum


    for i in range(256):
        for j in range(len(map[i])):
            current_value += (i+1)*(j+1)*int(map[i][j].split('=')[1])
            print(i+1, j+1, map[i][j], (i+1)*(j+1)*int(map[i][j].split('=')[1]))

    print(current_value)


with open('input.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    
    line = lines[0]
    words = line.split(',')


    current_value = 0

    for word in words:
        word_sum = 0
        for char in word:
            word_sum += ord(char)
            word_sum *= 17
            word_sum %= 256
        current_value += word_sum
    print(current_value)


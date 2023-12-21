def get_type(hand):
    counter = [0]*15

    joker_counter = 0
    for char in hand:
        if char == '1': # Joker
            joker_counter += 1
        else:
            counter[int(char, 16)] += 1

    largest_index = counter.index(max(counter))
    counter[largest_index] += joker_counter

    if 5 in counter:
        return 7
    elif 4 in counter:
        return 6
    elif 3 in counter and 2 in counter:
        return 5
    elif 3 in counter:
        return 4
    elif 2 in counter and counter.count(2) == 2:
        return 3
    elif 2 in counter:
        return 2
    else:
        return 1

def card_value(hand1):
    type1 = get_type(hand1)
    card_value1 = int(f"{type1}" + hand1, 16)
    return card_value1

with open('input.txt', 'r') as f:
    lines = f.readlines()
    lines = [line.strip().split(' ') for line in lines]
    for line in lines:
        line[0] = line[0].replace('A', 'E')
        line[0] = line[0].replace('T', 'A')
        line[0] = line[0].replace('J', '1')
        line[0] = line[0].replace('Q', 'C')
        line[0] = line[0].replace('K', 'D')

    lines.sort(key=lambda x: card_value(x[0]))

    winnings = 0

    for i in range(len(lines)):
        winnings += (i + 1) * int(lines[i][1])

    print(winnings)


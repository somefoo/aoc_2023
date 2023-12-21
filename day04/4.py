with open("input.txt") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    lines = [" ".join(line.split()) for line in lines]

    points = 0

    for line in lines:
        card = line.split(":")
        card = card[1].split("|")

        win_numbers = set([int(i) for i in card[0].strip().split(" ")])
        elf_numbers = set([int(i) for i in card[1].strip().split(" ")])

        winnings = win_numbers & elf_numbers

        if len(winnings) > 0:
            points += 2**(len(winnings) - 1)
    print(points)

with open("input.txt") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    lines = [" ".join(line.split()) for line in lines]
    original_lines = lines.copy()

    points = 0
    for line in lines:
        card = line.split(":")
        card_number = int(card[0].strip().split(" ")[1])

        card = card[1].split("|")

        win_numbers = set([int(i) for i in card[0].strip().split(" ")])
        elf_numbers = set([int(i) for i in card[1].strip().split(" ")])

        winnings = win_numbers & elf_numbers

        if len(winnings) > 0:
            lines += original_lines[card_number: card_number + len(winnings)]

        print(len(lines))
        points = len(lines)

    print(points)

with open("input2.txt") as f:
    lines = f.readlines()
    lines = [" ".join(line.split(" ")) for line in lines]


    list_of_cards = []
    list_of_winning_numbers = []
    list_of_elfs_numbers = []

    for line in lines:
        card = line.split(":")
        list_of_cards.append(card[0].strip())

        card = card[1].split("|")
        print(card)

        win_numbers = [int(i) for i in card[0].strip().split(" ")]
        elf_numbers = [int(i) for i in card[1].strip().split(" ")]

        print(win_numbers)




        

    print(list_of_winning_numbers)

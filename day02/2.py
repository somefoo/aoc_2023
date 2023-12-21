with open("input.txt") as f:
    lines = f.readlines()
    valid_games = []

    for line in lines:
        game_number, rounds = int(line.split(":")[0][5:].strip()), line.split(":")[1].strip()
        rounds = [d.strip() for d in rounds.split(";")]

        for round in rounds:
            values = {"red":12, "green":13, "blue":14}
            draws = [d.strip().split(" ") for d in round.split(",")]
            for draw in draws:
                values[draw[1]] = values[draw[1]] - int(draw[0])

            if values["red"] < 0 or values["green"] < 0 or values["blue"] < 0:
                break
        else:
            valid_games.append(game_number)
            print(game_number)

    print(sum(valid_games))

with open("input.txt") as f:
    lines = f.readlines()
    powers = []

    for line in lines:
        game_number, rounds = int(line.split(":")[0][5:].strip()), line.split(":")[1].strip()
        rounds = [d.strip() for d in rounds.split(";")]
        multiple = 0

        values = {"red":0, "green":0, "blue":0}
        for round in rounds:
            draws = [d.strip().split(" ") for d in round.split(",")]
            for draw in draws:
                values[draw[1]] = max(int(draw[0]), values[draw[1]])
        power = values["red"] * values["green"] * values["blue"]
        powers.append(power)

    print(sum(powers))


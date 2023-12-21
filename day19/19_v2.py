with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]
    # Find line that is only ""
    for i, line in enumerate(lines):
        if line == "":
            break
    workflow = lines[:i]
    parts = lines[i + 1 :]



    wl = {}
    for w in workflow:
        open_bracket = w.find("{")
        name = w[:open_bracket]
        inside = w[open_bracket + 1 : -1]

        # Instruction list
        instructions = []
        for ins in inside.split(","):
            if ':' in ins:
                condition, rvalue = ins.split(':')
                char = condition[0]
                eq = condition[1]
                value = int(condition[2:])
                index = ['x','m','a','s'].index(char)
                if eq == '<':
                    instructions.append(lambda xmas, *,value=value, rvalue=rvalue, index=index: (xmas[index] < value) * rvalue)
                else:
                    instructions.append(lambda xmas, *,value=value, rvalue=rvalue, index=index: (xmas[index] > value) * rvalue)
            else:
                instructions.append(lambda xmas, *,ins=ins: ins)

        wl[name] = instructions

    # Create an working set for each workflow
    working_list = {name: [] for name in wl.keys() }

    for part in parts:
        part = part[1:-1]
        part = part.split(",")
        part = [int(p[2:]) for p in part]
        working_list['in'].append(part)


    part_sum = 0
    for part in working_list['in']:
        string = 'in'
        while not (string in ['A', 'R']):
            for ins in wl[string]:
                rvalue = ins(part)
                if rvalue:
                    string = rvalue
                    break

        if string == 'A':
            part_sum += sum(part)


    print(part_sum)


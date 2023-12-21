class IntervalObject:
    def __init__(self):
        self.ind = [[1, 4000], [1, 4000], [1, 4000], [1, 4000]]

    def copy(self):
        new = IntervalObject()
        new.ind = [i[:] for i in self.ind]
        return new

    def apply_split(self, conditions, all_conditions):
        if type(conditions) == list:
            condition = conditions[0]
        else:
            condition = conditions

        if condition[0] == 'A':
            return (self.ind[0][1] - self.ind[0][0] + 1) * (self.ind[1][1] - self.ind[1][0] + 1) * (self.ind[2][1] - self.ind[2][0] + 1) * (self.ind[3][1] - self.ind[3][0] + 1)
        elif condition[0] == 'R':
            return 0

        elif not ':' in condition:
            return self.apply_split(all_conditions[condition], all_conditions)


        condition, rvalue = condition.split(':')
        char = condition[0]
        eq = condition[1]
        value = int(condition[2:])
        index = ['x','m','a','s'].index(char)

        # TODO check the +/-1
        if eq == '<':
            excluded = self.copy()
            excluded.ind[index][0] = value
            self.ind[index][1] = value - 1

            return self.apply_split(rvalue, all_conditions) + excluded.apply_split(conditions[1:], all_conditions)
        else: # self > value
            excluded = self.copy()
            excluded.ind[index][1] = value
            self.ind[index][0] = value + 1

            return self.apply_split(rvalue, all_conditions) + excluded.apply_split(conditions[1:], all_conditions)



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
        instructions = [instruction.strip() for instruction in inside.split(",")]
        wl[name] = instructions

    # Create an working set for each workflow
    working_list = {name: [] for name in wl.keys() }

    a = IntervalObject()

    possibilities = a.apply_split('in', wl)

    print(possibilities)

with open("input.txt") as f:
    lines = [line.strip().split(" -> ") for line in f.readlines()]

    broadcaster = filter(lambda x: x[0] == 'broadcaster', lines)
    broadcaster = [b[1].split(', ') for b in lines if b[0] == 'broadcaster'][0]
    inst = {line[0][1:]:(line[0][0], [], [], line[1].split(", ")) for line in lines if line[0] != 'broadcaster'}

    terminal_inst = {}

    for key in inst:
        destination = inst[key][3]
        for d in destination:
            if not d in inst:
                terminal_inst[d] = ('%', [], [], [])
            else:
                inst[d][2].append(key)
                inst[key][1].append(0)

    inst = {**inst, **terminal_inst}

    #for destination in broadcaster:
    #    inst[destination][2].append('broadcaster')

    # instance: (key: (type, [input_values], [input_nodes], [output_nodes])

    inst.update({'broadcaster': ('broadcaster',[0], [], broadcaster)})

    #inst = {line[0][1:]:(line[0][0], line[1].split(", ")) for line in lines}

    print(broadcaster)
    print(inst)


    print("####################")
    #% Flip-flop, ignores inputs different from current state, flips state on input that is same and outputs new state
    #& Conjunction, outputs 1 if all inputs are 1, otherwise 0


    class flip_flop:
        def __init__(self, input_nodes, output_nodes):
            self.state = 0
            self.input_nodes = input_nodes
            self.output_nodes = output_nodes
        def tick(self, source, value):
            if value == 0:
                self.state = 1 - self.state
                return [(output, self.state) for output in self.output_nodes]
            return []
        def __repr__(self):
            return "Flip-flop: " + str(self.state)

    class conjunction:
        def __init__(self, input_nodes, output_nodes):
            self.input_nodes = input_nodes
            self.output_nodes = output_nodes
            self.state = {node:0 for node in input_nodes}
        def tick(self, source, value):
            if source in self.state:
                self.state[source] = value
            if all(self.state.values()):
                return [(output, 0) for output in self.output_nodes]
            else:
                return [(output, 1) for output in self.output_nodes]
            return []
        def __repr__(self):
            return "Conjunction: " + str(self.state)
    class broadcaster:
        def __init__(self, input_nodes, output_nodes):
            self.input_nodes = input_nodes
            self.output_nodes = output_nodes
            self.state = 0
        def tick(self, source, value):
            return [(output, self.state) for output in self.output_nodes]
        def __repr__(self):
            return "Broadcaster"

    flip_flop_inst = {key:flip_flop(inst[key][2], inst[key][3]) for key in inst if inst[key][0] == '%'}
    conjunction_inst = {key:conjunction(inst[key][2], inst[key][3]) for key in inst if inst[key][0] == '&'}
    broadcaster_inst = {key:broadcaster(inst[key][2], inst[key][3]) for key in inst if inst[key][0] == 'broadcaster'}

    inst = {**flip_flop_inst, **conjunction_inst, **broadcaster_inst}


    low_sent = 0
    high_sent = 0

    for i in range(0,1000):

        received_signal = [('button' ,'broadcaster', 0)]
        while received_signal:
            current = received_signal.pop(0)
            source, destination, value = current
            if value == 0:
                low_sent += 1
            else:
                high_sent += 1

            a = "-low" if value == 0 else "-high"
            print(f"{source} {a}->{destination}")
            #print(inst)

            is_conjunction = inst[destination].__class__.__name__ == 'conjunction'

            for new_signal in inst[destination].tick(source, value):
                received_signal.append((destination, new_signal[0], new_signal[1]))

            #from time import sleep
            #sleep(2)

    print(low_sent, high_sent)
    print(low_sent * high_sent)

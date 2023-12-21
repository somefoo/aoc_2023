with open("input2.txt") as f:
    lines = [line.strip().split(" -> ") for line in f.readlines()]

    broadcaster = filter(lambda x: x[0] == 'broadcaster', lines)
    broadcaster = [b[1].split(', ') for b in lines if b[0] == 'broadcaster'][0]
    inst = {line[0][1:]:(line[0][0], [], [], line[1].split(", ")) for line in lines if line[0] != 'broadcaster'}

    for key in inst:
        destination = inst[key][3]
        for d in destination:
            inst[d][2].append(key)
            inst[key][1].append(0)
    #for destination in broadcaster:
    #    inst[destination][2].append('broadcaster')

    # instance: (key: (type, [input_values], [input_nodes], [output_nodes])

    inst.update({'broadcaster': ('broadcaster',[0], [], broadcaster)})

    #inst = {line[0][1:]:(line[0][0], line[1].split(", ")) for line in lines}

    print(broadcaster)
    print(inst)


    #% Flip-flop, ignores inputs different from current state, flips state on input that is same and outputs new state
    #& Conjunction, outputs 1 if all inputs are 1, otherwise 0

    low_sent, high_sent = 0, 0

    #for destination in broadcaster:
    #    inst[destination][1].append(0)
    #    low_sent += 1



    def do_tick(tick, received_signal):
        low_sent = 0
        high_sent = 0
        to_fill = []
        new_received_signal = []
        for key in inst:
            if not key in received_signal:
                continue
            instruction = inst[key]
            typei, inputs, input_nodes, output_nodes = instruction

            if typei == 'broadcaster':
                if inputs != []:
                    for output in output_nodes:
                        print(f"{typei}{key} {inputs[0]}-> {output}")
                        to_fill.append((output, inputs[0], key))
                    inst[key][1].pop(0)

            if typei == '%':
                if len(inputs) >= 2:
                    if inputs[0] == inputs[1]:
                        for output in output_nodes:
                            to_fill.append((output, 1-inputs[0], key))
                            if inputs[0] == 1:
                                print(f"{typei}{key} -low-> {output}")
                            else:
                                print(f"{typei}{key} -high-> {output}")
                        inst[key][1].pop(0)
                        inst[key][1][0] = 1-inputs[0]
                    #else:
                    #    for output in output_nodes:
                    #        to_fill.append((output, inputs[0]))
                    #        if inputs[0] == 1:
                    #            print(f"{typei}{key} -high-> {output}")
                    #        else:
                    #            print(f"{typei}{key} -low-> {output}")
                    #    inst[key][1].pop(-1)
            if typei == '&':
                if all(inputs):
                    for output in output_nodes:
                        to_fill.append((output, 0, key))
                        print(f"{typei}{key} -low-> {output}")
                else:
                    for output in output_nodes:
                        to_fill.append((output, 1, key))
                        print(f"{typei}{key} -high-> {output}")
                    #inst[key][1].clear()
        for tf in to_fill:
            if inst[tf[0]][0] == '&':
                # Get index of key in input_nodes of destination
                index = inst[tf[0]][2].index(tf[2])
                inst[tf[0]][1][index] = tf[1]

            else:
                inst[tf[0]][1].append(tf[1])
            new_received_signal.append(tf[0])

            if tf[1] == 1: high_sent += 1
            else: low_sent += 1
            #print("Filling", tf[0], "->", tf[1])

        from time import sleep
        sleep(3)
        print("#")
        return low_sent, high_sent, new_received_signal



    received_signal = ['broadcaster']
    for i in range(0, 1000):
        ls, hs, received_signal = do_tick(0, received_signal)
        low_sent += ls
        high_sent += hs

        #for key in inst:
        #    instruction = inst[key]
        #    print(key, instruction)

        if ls == 0 and hs == 0:
            print("Done at tick", i)
            break

    print(low_sent, high_sent)

    exit()





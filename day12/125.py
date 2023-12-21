with open('input2.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

    sum = 0
    sum2 = 0
    for line in lines[0:1]:
        line, wanted = line.split(' ')
        wanted = [int(x) for x in wanted.split(',')]
        line = line + "."
        #print(line, wanted)

        def dive(text, block, wanted) -> int:
            print(text, block, wanted)
            #if len(text) == 0 and wanted == []:
            #    print("FOUND")
            #    return 1
            if len(text) == 0:
                return 0
            #if wanted == [] and "#" in text:
            #    return 0
                #if wanted == [] and "#" not in text:
                #    print("FOUND")
                #    return 1
                #if len(text) == 0:
                #    if block == wanted[0]:
                #        print("FOUND")
                #        return 1
                #    else:
                #        print("XXXX")
                #        return 0

            if text[0] == '.':
                if text == '.' and wanted == []:
                    return 1
                if block == wanted[0]:
                    return dive(text[1:], 0, wanted[1:])
                elif block == 0:
                    # Prevent #.##.### (2) 2,3 from being accepted
                    return dive(text[1:], 0, wanted)
                else:
                    return 0
            elif text[0] == '#':
                return dive(text[1:], block + 1, wanted)

            elif text[0] == '?':
                text_copy_dot = text
                text_copy_dot = '.' + text_copy_dot[1:]
                text_copy_hash = text
                text_copy_hash = '#' + text_copy_hash[1:]

                return dive(text_copy_dot, block, wanted) + dive(text_copy_hash, block, wanted)
            else:
                print("Fuck")
                return 0

        #dive_v = dive(line, 0, wanted)

        new_line = "?".join([line]*5)
        new_wanted = wanted * 5

        dive_v2 = dive(new_line, 0, new_wanted)

        #sum += dive_v
        sum2 += dive_v2
        #print(dive_v)
        print(dive_v2)

    print("SUM:  ", sum)
    print("SUM2: ", sum2)











    #    number_of_combinations = 0
    #
    #    for line in lines:
    #        original_line, wanted = line.split(' ')
    #        #original_line = "?".join([original_line]*2)
    #        #wanted = ",".join([wanted]*2)
    #        qmarks = original_line.count('?')
    #
    #        #wanted_count = [int(x) for x in wanted.split(',')]
    #
    #        ncb = 0
    #        for i in range(2**qmarks):
    #            edited_line = original_line
    #        # Get binary representation of i
    #            #binary = bin(i)[2:]
    #            binary = "{0:b}".format(i)
    #            fill_zeros = qmarks - len(binary)
    #            binary = '0' * fill_zeros + binary
    #            #print(binary)
    #
    #            #b2 = "{0:b}".format(i)
    #            #print(b2)
    #            # Go over each bit and replace ? with 0 or 1
    #            for bit in binary:
    #                edited_line = edited_line.replace('?', bit, 1)
    #
    #            # Replace all # with 1
    #            edited_line = edited_line.replace('#', '1')
    #            edited_line = edited_line.replace('.', '0')
    #
    #
    #            # Get all blocks of 1s
    #            blocks = edited_line.split('0')
    #            blocks = [str(len(block)) for block in blocks if block != '']
    #
    #            block_string = ','.join(blocks)
    #
    #            if block_string == wanted:
    #                ncb += 1
    #
    #
    #
    #        ncb2 = 0
    #        if original_line[-1] == '#':
    #            original_line = original_line + '?'
    #        else:
    #            original_line = '?' + original_line + '?'
    #        qmarks = original_line.count('?')
    #        for i in range(2**qmarks):
    #            edited_line = original_line
    #        # Get binary representation of i
    #            #binary = bin(i)[2:]
    #            binary = "{0:b}".format(i)
    #            fill_zeros = qmarks - len(binary)
    #            binary = '0' * fill_zeros + binary
    #            #print(binary)
    #
    #            #b2 = "{0:b}".format(i)
    #            #print(b2)
    #            # Go over each bit and replace ? with 0 or 1
    #            for bit in binary:
    #                edited_line = edited_line.replace('?', bit, 1)
    #
    #            # Replace all # with 1
    #            edited_line = edited_line.replace('#', '1')
    #            edited_line = edited_line.replace('.', '0')
    #
    #
    #            # Get all blocks of 1s
    #            blocks = edited_line.split('0')
    #            blocks = [str(len(block)) for block in blocks if block != '']
    #
    #            block_string = ','.join(blocks)
    #
    #            if block_string == wanted:
    #                ncb2 += 1
    #
    #        print(ncb2 * ncb2 * ncb2 * ncb2 * ncb)
    #        number_of_combinations += ncb2 * ncb2 * ncb2 * ncb2 * ncb
    #
    #
    #
    #print(number_of_combinations)

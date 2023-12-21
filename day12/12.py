


with open('input.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

    number_of_combinations = 0

    for line in lines:
        original_line, wanted = line.split(' ')
        qmarks = line.count('?')
        for i in range(2**qmarks):
            edited_line = original_line
        # Get binary representation of i
            #binary = bin(i)[2:]
            binary = "{0:b}".format(i)
            fill_zeros = qmarks - len(binary)
            binary = '0' * fill_zeros + binary
            #print(binary)

            #b2 = "{0:b}".format(i)
            #print(b2)
            # Go over each bit and replace ? with 0 or 1
            for bit in binary:
                edited_line = edited_line.replace('?', bit, 1)

            # Replace all # with 1
            edited_line = edited_line.replace('#', '1')
            edited_line = edited_line.replace('.', '0')


            # Get all blocks of 1s
            blocks = edited_line.split('0')
            blocks = [str(len(block)) for block in blocks if block != '']

            block_string = ','.join(blocks)

            if block_string == wanted:
                number_of_combinations += 1


print(number_of_combinations)

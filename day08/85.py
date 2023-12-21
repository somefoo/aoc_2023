import numpy as np
from numba import jit

import warnings

from numba.core.errors import NumbaDeprecationWarning, NumbaPendingDeprecationWarning

warnings.simplefilter('ignore', category=NumbaDeprecationWarning)
warnings.simplefilter('ignore', category=NumbaPendingDeprecationWarning)


with open('input.txt') as f:
    data = f.read().splitlines()

    directions = data[0]

    data = data[2:]

    # Remove all special characters (sometimes with space)
    data = [x.replace('(', '').replace(')', '').replace('= ', '').replace(',','') for x in data]




    starting_nodes = []
    for line in data:
        line = line.split()
        if line[0][2] == 'A':
            starting_nodes.append(line[0])




    ab = int('ZZZ', 36)

    nodes = [int(x, 36) for x in starting_nodes]
    left = np.zeros(ab + 1, dtype=int)
    right = np.zeros(ab + 1, dtype=int)
    z_at_end = np.zeros(ab + 1, dtype=bool)
    debug = ['' for _ in range(ab + 1)]



    def fill_array(left, right, input):
        for line in input:
            line = line.split()
            left[int(line[0], 36)] = int(line[1], 36)
            right[int(line[0], 36)] = int(line[2], 36)
            if line[0][-1] == 'Z':
                z_at_end[int(line[0], 36)] = True
                debug[int(line[0], 36)] = line[0]

    fill_array(left, right, data)


    @jit
    def run(nodes, action):
        if action == 'L':
            return [left[x] for x in nodes]
        else:
            return [right[x] for x in nodes]

    @jit
    def check_if_five_with_z(nodes):
        return all([z_at_end[x] for x in nodes])

    @jit
    def check(nodes, directions):
        i = 0
        while True:
            nodes = run(nodes, directions[i % len(directions)])

            i += 1
            if check_if_five_with_z(nodes):
                print('Found five with z')
                break

        print(i)

    check(nodes, directions)


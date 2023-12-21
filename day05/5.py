from numba import jit

class GNode():
    def __init__(self):
        self.destination = []
        self.source = []
        self.range_length = []

    def get_destination(self, current):
        for i in range(len(self.source)):
            if current in range(self.source[i], self.source[i] + self.range_length[i]):
                offest = current - self.source[i]
                return self.destination[i] + offest
        return current
    def get_source(self, current):
        for i in range(len(self.destination)):
            if current in range(self.destination[i], self.destination[i] + self.range_length[i]):
                offest = current - self.destination[i]
                return self.source[i] + offest
        return current

    def append(self, destination, source, length):
        self.destination.append(destination)
        self.source.append(source)
        self.range_length.append(length)


with open("input.txt") as f:
    graph = [GNode(), GNode(), GNode(), GNode(), GNode(), GNode(), GNode()]

    currently_read = -1
    seeds = []
    for line in f:
        line = line.strip()
        if line[0:6] == "seeds:":
            seeds = line[7:].strip().split(" ")
            seeds = [int(s) for s in seeds]
            continue

        if line == "":
            continue

        if "map:" in line:
            currently_read += 1
            continue

        dest_source_range = line.strip().split(" ")
        graph[currently_read].append(int(dest_source_range[0]), int(dest_source_range[1]), int(dest_source_range[2]))

    part1_seeds = seeds.copy()
    for i in range(7):
        part1_seeds = [graph[i].get_destination(s) for s in part1_seeds]

    min_dist = 3000000000
    for i in range(0, len(seeds), 2):
        print(i, seeds[i], seeds[i+1])
        for s in range(seeds[i], seeds[i] + seeds[i+1]):
            print((s - seeds[i])/seeds[i+1] * 100, "%")
            for j in range(7):
                s = graph[j].get_destination(s)
            min_dist = min(s, min_dist)
        #print("min so far: ", min_dist)
        #print(min_dist)


    def inside_range(value, seeds):
     for i in range(0, len(seeds), 2):
         if value in range(seeds[i], seeds[i] + seeds[i+1]):
             print("in range: ", value, seeds[i], seeds[i+1])
             return True
     return False

    for v in range(0, 100000000, 1):
        # Print progress
        print(v / 100000000 * 100, "%")
        seed = v
        for i in range(0, 7):
            seed = graph[6 - i].get_source(seed)

        if inside_range(seed, seeds):
            print("valid: ", seed, " with location: ", v)
            exit()

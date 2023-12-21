
def time_function(t_charge, t_total):
    t_left = t_total - t_charge #[s]
    #acceleration = t_charge # [m/s^2]


    # Constant acceleration
    end_speed = t_charge #[m/s]
    distance = t_left * end_speed #[m]

    return distance

def accel_time_function(t_charge, t_total):
    t_left = t_total - t_charge #[s]
    acceleration = t_charge # [m/s^2]

    # Constant acceleration
    end_speed = t_left * acceleration #[m/s]
    distance = t_left * end_speed/2 #[m]

    return distance

    # Acceleration = m/(s^2)




with open("input.txt") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    lines = ["".join(line.split()) for line in lines]

    time = [int(x) for x in lines[0].split(":")[1].strip().split(" ")]
    distance = [int(x) for x in lines[1].split(":")[1].strip().split(" ")]

    print(time)
    print(distance)

    ways_to_win = 1
    for i in range(len(time)):
        beat_times = []
        for charge_time in range(time[i] + 1):
            distance_travelled = time_function(charge_time, time[i])
            if distance_travelled > distance[i]:
                beat_times.append(charge_time)
            #print(charge_time, distance_travelled)
        ways_to_win *= len(beat_times)

    print(ways_to_win)

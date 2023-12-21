with open('input2.txt') as f:
    lines = [line.strip() for line in f]
    #lines = {x + y*1j:c for y, line in enumerate(lines) for x, c in enumerate(line)} 
    lines = {x + y*1j:(-1 if c == '.' else c) for y, line in enumerate(lines) for x, c in enumerate(line)} 


    width = max(int(x.real) for x in lines.keys())+1
    height = max(int(x.imag) for x in lines.keys())+1


    start = next(k for k, v in lines.items() if v == 'S')
    lines[start] = -1 # Temporarily remove start

    for repeat_y in range(-200, 201):
        for repeat_x in range(-200,201):
            if repeat_x == 0 and repeat_y == 0: continue
            for x in range(0,width):
                for y in range(0,height):
                    lines[x + y*1j + repeat_x*width + repeat_y*height*1j] = lines[x + y*1j]


    lines[start] = 0

    front = [start]
    even_counter = 1 # Include 0
    odd_counter = 0

    even_counter_list = []
    odd_counter_list = []

    for counter in range(1,2000+1):
        new_front = [] 
        for pos in front:
            for d in [1, -1, 1j, -1j]:
                if pos + d not in lines:
                    continue
                if lines[pos + d] == -1:
                    lines[pos + d] = counter
                    new_front.append(pos + d)
        if counter % 2 == 0:
            even_counter += len(new_front)
            even_counter_list.append(even_counter)
        else:
            odd_counter += len(new_front)
            odd_counter_list.append(odd_counter)
        front = new_front


    #Plot even_counter_list
    import matplotlib.pyplot as plt
    #even_counter_list = [even_counter_list[i] - even_counter_list[i-1] for i in range(1,len(even_counter_list))]
    #plt.plot(even_counter_list)

    ## Find e^x that fits the curve
    import numpy as np
    #from scipy.optimize import curve_fit
    #def func(x, a, b, c):
    #    #return a * np.exp(-b * x) + c
    #    return a * 2**(-b * x) + c
    #popt, pcov = curve_fit(func, np.arange(0,len(even_counter_list)), even_counter_list)

    #def func_opt(x):
    #    return func(x, *popt)

    #eval_list = [func_opt(x) for x in range(0,len(even_counter_list))]
    #plt.plot(eval_list)
    #plt.plot(even_counter_list)
    #plt.show()

    # Fit polynomial
    p = np.polyfit(np.arange(0,len(odd_counter_list)), odd_counter_list, 2)
    print(p)
    def func_poly(x):
        return p[0]*x**2 + p[1]*x + p[2]
    eval_list = [func_poly(x) for x in range(0,len(odd_counter_list))]
    plt.plot(eval_list)
    plt.plot(odd_counter_list)
    plt.show()

    print(func_poly(500/2))
    print(func_poly(1000/2))
    print(func_poly(5000/2))
    print(func_poly(5000/2))
    print(func_poly(26501365/2))

    #print(popt)

    #plt.plot(odd_counter_list)
    #sum_counter_list = [even_counter_list[i] + odd_counter_list[i] for i in range(len(even_counter_list))]
    #plt.plot(sum_counter_list)

    # show
    #plt.show()

    #sum_counter_list = [sum_counter_list[i] - sum_counter_list[i-1] for i in range(1,len(sum_counter_list))]
    #print(sum_counter_list)

    # Compute pairwise differences
    #even_counter_list = [even_counter_list[i] - even_counter_list[i-1] for i in range(1,len(even_counter_list))]
    #even_counter_list = [even_counter_list[i] - even_counter_list[i-1] for i in range(1,len(even_counter_list))]
    #print(even_counter_list)
    #odd_counter_list = [odd_counter_list[i] - odd_counter_list[i-1] for i in range(1,len(odd_counter_list))]
    #print(even_counter_list)
    #print(odd_counter_list)



    


    exit()

    for i in range(min(int(x.real) for x in lines.keys()),max(int(x.real) for x in lines.keys())+1):
        for j in range(min(int(x.imag) for x in lines.keys()),max(int(x.imag) for x in lines.keys())+1):
            if i + j*1j in lines:
                #print(str(lines[i + j*1j]).zfill(2), end=' ')
                print(str(lines[i + j*1j])[-1], end='')
        print("")





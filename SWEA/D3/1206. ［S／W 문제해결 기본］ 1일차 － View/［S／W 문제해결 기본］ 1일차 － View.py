for t in range(10) :
    length = int(input())
    N = list(map(int, input().split()))
    i = 2
    output = 0
    while (i<=(length-2)) :
        if (N[i] > N[i+1]) and (N[i] > N[i+2]) and (N[i] > N[i-1]) and (N[i] > N[i-2]) :
            output += (N[i] - max(N[i-1], N[i-2], N[i+1], N[i+2]))
            i += 3
        else :
            i += 1

    print('#{} {}'.format(t+1, output))
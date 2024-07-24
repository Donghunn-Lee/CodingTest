while True:
    each_side = list(map(int, input().split()))
    each_side.sort()

    if sum(each_side) == 0 :
        break
    
    if each_side[0] ** 2 + each_side[1] ** 2 == each_side[2] ** 2:
        print("right")
    else:
        print("wrong")
    
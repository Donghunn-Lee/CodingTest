# 혁진이의 프로그램 검증

from collections import deque


def direction(curval):
    v = curval
    d = ()

    if v == '>':
        d = (0, 1)
    elif v == 'v':
        d = (1, 0)
    elif v == '^':
        d = (-1, 0)
    elif v == '<':
        d = (0, -1)
    return d


def hyukSemblier (c, d):
    cur = c
    dr = d                          # [1, 0], [-1, 0], [0, -1], [0, 1] 각각 상, 하, 좌, 우
    w_str = '<>^v'
    m = 0
    v_arr = {(c, dr, m)}
    q = deque()
    q.append((cur, dr, m))

    while q:
        cur, dr, m = q.popleft()

        if arr[cur[0]][cur[1]] in w_str:
            dr = direction(arr[cur[0]][cur[1]])

        elif arr[cur[0]][cur[1]] == '_':
            if m == 0:
                dr = (0, 1)
            else:
                dr = (0, -1)

        elif arr[cur[0]][cur[1]] == '|':
            if m == 0:
                dr = (1, 0)
            else:
                dr = (-1, 0)

        elif arr[cur[0]][cur[1]] == '@':
            return 'YES'

        elif arr[cur[0]][cur[1]] in map(str, range(10)):
            m = int(arr[cur[0]][cur[1]])

        elif arr[cur[0]][cur[1]] == '+':
            if m == 15:
                m = 0
            else:
                m += 1

        elif arr[cur[0]][cur[1]] == '-':
            if m == 0:
                m = 15
            else:
                m -= 1

        if arr[cur[0]][cur[1]] == '?':
            for r in w_str:
                n_dr = direction(r)
                n_cur = ((cur[0]+n_dr[0]) % R, (cur[1]+n_dr[1]) % C)

                if (n_cur, n_dr, m) not in v_arr:
                    v_arr.add((n_cur, n_dr, m))
                    q.append((n_cur, n_dr, m))
                    
        else:
            n_cur = ((cur[0]+dr[0]) % R, (cur[1]+dr[1]) % C)
            if (n_cur, dr, m) not in v_arr:
                v_arr.add((n_cur, dr, m))
                q.append((n_cur, dr, m))

    return 'NO'


T = int(input())

for t in range(1, T+1):
    R, C = map(int, input().split())
    arr = [input() for _ in range(R)]

    ans = hyukSemblier((0, 0), (0, 1))

    print(f"#{t} {ans}")
    
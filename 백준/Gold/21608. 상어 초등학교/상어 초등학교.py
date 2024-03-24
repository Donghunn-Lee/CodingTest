# 상어 초등학교

n = int(input())
if n >= 3 and n <= 20 :
    score = 0
    seat = [[0] * n for _ in range(n)]
    st_dict = {}

    for _ in range(n * n):
        st_num, *fav_friends = map(int, input().split())
        st_dict[st_num] = fav_friends

        result = [n,n]
        max_fr, max_blank = 0, 0
        for c in range(n):
            for r in range(n):
                if seat[c][r] == 0:
                    cross = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # left, right, up, down
                    fr_count, blank = 0, 0
                    for k in cross:
                        new_c, new_r = c + k[1], r + k[0]
                        if 0 <= new_c < n and 0 <= new_r < n:
                            if seat[new_c][new_r] in fav_friends:
                                fr_count += 1
                            if seat[new_c][new_r] == 0:
                                blank += 1

                    if max_fr < fr_count or (max_fr == fr_count and max_blank < blank):
                        max_blank = blank
                        max_fr = fr_count
                        result = [c, r]

                    if max_fr + max_blank == 0:
                        if c < result[0] :
                            if r < result[1] :
                                result = [c, r]
                        elif c == result[0] :
                            if r < result[1] :
                                result = [c, r]


        seat[result[0]][result[1]] = st_num

    for c in range(n):
        for r in range(n):
            cross = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # left, right, up, down
            fr_count = 0
            for k in cross:
                new_c, new_r = c + k[1], r + k[0]
                if 0 <= new_c < n and 0 <= new_r < n:
                    if seat[new_c][new_r] in st_dict[seat[c][r]]:
                        fr_count += 1

            if fr_count == 1:
                score += 1
            elif fr_count == 2:
                score += 10
            elif fr_count == 3:
                score += 100
            elif fr_count == 4:
                score += 1000
                
    print(score)
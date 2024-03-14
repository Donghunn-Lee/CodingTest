# 나는야 포켓몬 마스터 이다솜

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().split())
    poketmon_dict = {k : input().rstrip() for k in range(1, N + 1)}
    reversed_dict = {v : k for k, v in poketmon_dict.items()}

    question = [input().rstrip() for _ in range(M)]
    ans = []
    
    for q in question:
        if q.isalpha():
            ans.append(reversed_dict.get(q))
        else:
            ans.append(poketmon_dict.get(int(q)))
    
    sys.stdout.write("\n".join(map(str, ans)))
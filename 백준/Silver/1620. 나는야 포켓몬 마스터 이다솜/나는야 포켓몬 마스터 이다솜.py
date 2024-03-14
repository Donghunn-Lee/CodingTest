# 나는야 포켓몬 마스터 이다솜

# 실버 4기도 하고 진짜 쉬워보였는데 시간초과가 나서 살짝 당황.
# index로 찾는 게 문제인가 싶어 딕셔너리에서 값으로 키를 찾는 방법을 검색.
# 그 결과 키와 벨류가 반대로 된 새 딕셔너리를 만드는 방법이 있다는 것을 알게 됨.
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().split())
    poketmon_dict = {k : input().rstrip() for k in range(1, N + 1)}
    reversed_dict = {v : k for k, v in poketmon_dict.items()}   # 키와 벨류가 뒤집어진 딕셔러니 생성.

    question = [input().rstrip() for _ in range(M)]
    ans = []
    
    for q in question:
        if q.isalpha(): # 알파벳이 아니라면 숫자이므로
            ans.append(reversed_dict.get(q))
        else:
            ans.append(poketmon_dict.get(int(q)))
    
    sys.stdout.write("\n".join(map(str, ans)))
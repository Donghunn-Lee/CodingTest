# 나머지

A, B, C = map(int, input().split())

ans = []

ans.append((A+B)%C)
ans.append(((A%C)+(B%C))%C)
ans.append((A*B)%C)
ans.append(((A%C)*(B%C))%C)

for i in ans:
    print(i)

ans = []

while True:
    N = list(input().rstrip())

    if N == ['0']:
        break

    if N == list(reversed(N)):
        ans.append("yes")
    else:
        ans.append("no")
    
print("\n".join(ans))
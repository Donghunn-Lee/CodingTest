# 방울 마술

def predict(s, n):
    tmp = s

    for _ in range(n):
        if tmp == '.o.':
            tmp = 'o.o'
        elif tmp == 'o.o' or tmp == 'o..' or tmp == '..o':
            tmp = '.o.'
    
    for i in range(3):
        if tmp[i] == 'o':
            return i


if __name__ == "__main__":
    T = int(input())
    ans = []

    for t in range(1, T + 1):
        S, N = input().split()
        ans.append(f'#{t} {predict(S, int(N))}')
    
    print("\n".join(ans))
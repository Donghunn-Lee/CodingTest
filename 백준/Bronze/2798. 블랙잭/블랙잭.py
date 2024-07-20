
def sol(n):
    max_sum = 0

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                tmp = seq[i] + seq[j] + seq[k]

                if tmp <= M:
                    max_sum = max(max_sum, tmp)
                    
    return max_sum
            


if __name__ == "__main__":
    N, M = map(int, input().split())
    seq = list(map(int, input().split()))
    
    print(sol(N))
    
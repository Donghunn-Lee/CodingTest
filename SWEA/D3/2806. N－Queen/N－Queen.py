def is_safe(ci):
    for i in range(ci):
        if board_row[i] == board_row[ci] or abs(board_row[i] - board_row[ci]) == abs(i - ci):
            return False
        
    return True

def put_the_queen(i):
    global ans

    if i == N:
        ans += 1
        return
    
    for j in range(N):
        board_row[i] = j

        if is_safe(i):
            put_the_queen(i + 1)

if __name__ == "__main__":
    T = int(input())
    output = []

    for t in range(1, T + 1):
        N = int(input())
        board_row = [0] * N
        ans = 0

        put_the_queen(0)

        output.append(f'#{t} {ans}')
    
    print("\n".join(output))
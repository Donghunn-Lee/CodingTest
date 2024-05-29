N, M = map(int, input().split())
apps = list(map(int, input().split()))
deact = list(map(int, input().split()))

# dp[비용][메모리]
dp = [[0 for _ in range(10000+1)] for _ in range(N+1)]
for i in range(1, N+1): # i 개의 앱 비활성화
    for w in range(10000+1): # 사용 가능한 비활성화에 필요한 비용
        if deact[i-1] <= w: # i-1 개의(리스트 시작 인덱스 = 1) 앱을 비활성화 시킬 수 있다면 
        	# i개 비활성화로 확보된 메모리 = i-1 개 비활성화 + i-1 번 째 앱 메모리 (i-1 번째 비활성화)
            # 						    i-1 번째 비활성화 X 중 최댓값
            dp[i][w] = max(apps[i-1] + dp[i-1][w-deact[i-1]], dp[i-1][w])
        else: # 비활성화 불가
            dp[i][w] = dp[i-1][w]

for i, c in enumerate(dp[-1]): # 
    if c >= M: # 처음으로 필요한 메모리보다 확보된 양이 많아진다면 출력
        print(i)
        break
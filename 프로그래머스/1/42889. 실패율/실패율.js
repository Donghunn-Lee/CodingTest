function solution(N, stages) {
    let result = Array(N).fill(0);
    const failureRate = Array.from(Array(N), (_, i) => [i + 1, 0])
    const clearRate = Array(N + 1).fill(0);
    const arriveRate = Array(N + 1).fill(0);
    
    stages.forEach((v, i) => {
        for (let j = 1; j <= v; j++) {
            clearRate[j] += 1;
        }
        
        arriveRate[v] += 1;
    })
    
    for (let i = 0; i < N; i++) {
        failureRate[i][1] = arriveRate[i + 1] / clearRate[i + 1];
    }
    
        // 실패율 기준으로 내림차순 정렬 (같으면 스테이지 번호 오름차순)
    failureRate.sort((a, b) => b[1] - a[1] || a[0] - b[0]);

    // 정렬된 스테이지 번호만 반환
    return failureRate.map(v => v[0]);
    
}
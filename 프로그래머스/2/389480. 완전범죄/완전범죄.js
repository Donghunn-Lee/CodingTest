function solution(info, n, m) {
    const infoLength = info.length;
    const dp = Array.from({length : infoLength + 1}, () => Array(m).fill(Infinity));
    
    dp[0][0] = 0;
    
    for (let i = 0; i < infoLength; i++) {
        const [pa, pb] = info[i];
        
        for (let b = 0; b < m; b++) {
            if (dp[i][b] == Infinity) continue;
            
            const sumA = dp[i][b] + pa;
            if (sumA < n) {
                dp[i + 1][b] = Math.min(dp[i + 1][b], sumA)
            }
            
            const sumB = b + pb;
            if (sumB < m) {
                dp[i + 1][sumB] = Math.min(dp[i + 1][sumB], dp[i][b])
            }
            
        }
    }
    
    let answer = Infinity;
    for (let b = 0; b < m; b++) {
        answer = Math.min(answer, dp[infoLength][b]);
    }
    
    return answer === Infinity ? -1 : answer;
    
}
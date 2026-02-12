function solution(board, skill) {
    let answer = 0;
    
    const N = board.length;
    const M = board[0].length;
    
    const acc = Array.from({length: N + 1}, () => Array(M + 1).fill(0))
    
    for (let [type, r1, c1, r2, c2, degree] of skill) {
        degree = type === 1 ? -degree : degree;
        
        acc[r1][c1] += degree;
        acc[r1][c2 + 1] -= degree;
        acc[r2 + 1][c1] -= degree;
        acc[r2 + 1][c2 + 1] += degree;
        
    }
    
    for (let i = 0; i < N; i++) {
        for (let j = 1; j < M; j++) {
            acc[i][j] += acc[i][j - 1]
        }
    }
    
    for (let i = 1; i < N; i++) {
        for (let j = 0; j < M; j++) {
            acc[i][j] += acc[i - 1][j]
        }
    }
    
    for (let i = 0; i < N; i++) {
        for (let j = 0; j < M; j++) {
            if (board[i][j] + acc[i][j] > 0) {
                answer++;
            }
        }
    }
    
    
    return answer;
}
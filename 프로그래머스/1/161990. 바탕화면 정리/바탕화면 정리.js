function solution(wallpaper) {
    let N = wallpaper.length, M = wallpaper[0].length;
    var answer = [N, M, 0, 0];
    
    for (let i = 0; i < N; i++) {
        for (let j = 0; j < M; j++) {
            if (wallpaper[i][j] === '#') {
                answer[0] = Math.min(i, answer[0]);
                answer[1] = Math.min(j, answer[1]);
                answer[2] = Math.max(i + 1, answer[2]);
                answer[3] = Math.max(j + 1, answer[3]);
            }
        }
    }
    
    return answer;
}
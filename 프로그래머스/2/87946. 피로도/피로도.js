function solution(k, dungeons) {
    let answer = -1;
    const n = dungeons.length;
    const visited = Array(n).fill(0);
    
    function dfs (fatigue, count) {
        for (let i = 0; i < n; i++) {
            if (!visited[i] && dungeons[i][0] <= fatigue) {
                visited[i] = 1;
                dfs(fatigue - dungeons[i][1], count + 1);
                visited[i] = 0;
            }
        }
        
        answer = Math.max(answer, count);
    }
    
    for (let i = 0; i < n; i++) {
        if (!visited[i] && dungeons[i][0] <= k) {
            visited[i] = 1;
            dfs(k - dungeons[i][1], 1);
            visited[i] = 0;
        }
    }
    
    return answer;
}


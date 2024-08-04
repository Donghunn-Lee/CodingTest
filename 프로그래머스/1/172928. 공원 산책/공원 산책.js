function locate (graph, N, M) {
    for (let i = 0; i < N; i++) {
        for (let j = 0; j < M; j++) {
            if (graph[i][j] === 'S') {
                return [i, j];
            }
        }
    }
}

function solution(park, routes) {
    let N = park.length, M = park[0].length;
    let cur = locate(park, N, M);
    let dir = {'N' : [-1, 0],
               'S' : [1, 0],
               'W' : [0, -1],
               'E' : [0, 1]};
    
    routes = routes.map((e) => e.split(" "))
    
    for (const cmd of routes) {
        let di = dir[cmd[0]][0], dj = dir[cmd[0]][1];
        let num = cmd[1];
        var ni = cur[0] + di * num;
        var nj = cur[1] + dj * num;
        
        if (0 <= ni && ni < N && 0 <= nj && nj < M) {
            let flag = true;
            ni = cur[0], nj = cur[1];
            
            for (let i = 0; i < num; i++) {
                ni += di, nj += dj;
                if (park[ni][nj] === 'X') {
                    flag = false;
                    break;
                }
            }
            
            if (flag) cur = [ni, nj];
        }
        
    }
    
    return cur;
}
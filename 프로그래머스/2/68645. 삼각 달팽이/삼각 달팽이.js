function solution(n) {
    const arr = Array.from({length : n}, (_, i) => Array(i + 1).fill(0))
    
    const dirs = [[1, 0], [0, 1], [-1, -1]];
    
    let r = -1;
    let c = 0;
    let num = 1;
    let dir = 0;
    
    for (let len = n; len > 0; len--) {
        for (let i = 0; i < len; i++) {
            r += dirs[dir][0];
            c += dirs[dir][1];
            arr[r][c] = num++;
        }
        
        dir = (dir + 1) % 3;
    }
    
    return arr.flat();
}
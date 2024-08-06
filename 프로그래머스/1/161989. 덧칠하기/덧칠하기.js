function solution(n, m, section) {
    let count = 0;
    let wall = Array(n + 1).fill(1);
    for (const i of section) {
        wall[i] = 0;
    }
    
    
    for (let i = 1; i < n + 1; i++) {
        if (wall[i] === 0) {
            i += m - 1;
            count += 1;
        }
    }
    
    return count;
}
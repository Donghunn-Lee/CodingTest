function solution(n, left, right) {
    const arr = []
    
    for (let i = left; i <= right; i++) {
        const val = Math.max(Math.floor(i / n), i % n) + 1;
        arr.push(val);
    }
    
    return arr;
}
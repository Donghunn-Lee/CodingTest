function solution(storey) {
    let cost = 0;
    let n = storey
    
    while (n) {
        const d = n % 10;
        
        if (d < 5) {
            cost += d;
            n = Math.floor(n / 10);
        } else if (d > 5) {
            cost += 10 - d;
            n = Math.floor(n / 10) + 1;
        } else {
            const next = Math.floor(n / 10) % 10;
            cost += 5;
            n = Math.floor(n / 10) + (next >= 5 ? 1 : 0);
        }
    }
    
    return cost;
}
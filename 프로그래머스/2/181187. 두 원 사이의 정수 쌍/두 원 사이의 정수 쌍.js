function solution(r1, r2) {
    let answer = 0;
    
    for (let i = 1; i <= r2; i++) {
        const maxX = Math.floor(Math.sqrt(r2 ** 2 - i ** 2));
        const minX = r1 > i ? Math.ceil(Math.sqrt(r1 ** 2 - i ** 2)) : 0;
        
        answer += (maxX - minX + 1);
    }
    
    return answer * 4;
}
function solution(elements) {
    let answer = new Set();
    const n = elements.length;
    
    elements = [...elements, ...elements];
    
    for (let i = 1; i <= n; i++){
        for (let j = 0; j < n; j++) {
            answer.add(elements.slice(j, j + i).reduce((acc, cur) => acc + cur, 0));
        }
    }
        
    return answer.size;
}
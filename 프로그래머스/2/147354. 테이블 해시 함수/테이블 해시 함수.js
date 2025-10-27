function solution(data, col, row_begin, row_end) {
    let answer = 0;
    const colLen = data[0].length;
    data.sort((a, b) => a[col - 1] - b[col - 1] || b[0] - a[0]);
    
    for (let i = row_begin - 1; i < row_end; i++) {
        let sum = 0;
        
        for (let j = 0; j < colLen; j++) {
            sum += data[i][j] %  (i + 1);
        }
        
        answer ^= sum;
    }
    
    return answer;
}
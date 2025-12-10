function solution(expression) {
    const prior = [
        ['-', '*', '+'], ['-', '+', '*'],
        ['*', '-', '+'], ['*', '+', '-'],
        ['+', '-', '*'], ['+', '*', '-']
    ];

    let answer = 0;
    
    for (let opCandidate of prior) {
        const tempNums = expression.split(/[^0-9]/).map(Number);
        const tempOps = expression.match(/[\+\-\*]/g);
        
        for (let op of opCandidate) {
            let idx = tempOps.indexOf(op);
            
            while (idx !== -1) {
                const num1 = tempNums[idx];
                const num2 = tempNums[idx + 1];
                let res = 0;
                
                if (op === '*') res = num1 * num2;
                else if (op === '+') res = num1 + num2;
                else if (op === '-') res = num1 - num2;
                
                tempNums.splice(idx, 2, res);
                tempOps.splice(idx, 1);
                idx = tempOps.indexOf(op);
            }
        }
        
        if (Math.abs(tempNums[0]) > answer) {
            answer = Math.abs(tempNums[0])
        }
    }
    
    return answer;
}
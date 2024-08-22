function numsInit(numString) {
    const nums = Array(10).fill(0);
    
    for (const char of numString) {
        nums[parseInt(char)]++;
    }
    
    return nums;
}

function solution(X, Y) {
    let answer = '';
    
    const xNums = numsInit(X);
    const yNums = numsInit(Y);
    
    for (let i = 9; i >= 0; i--) {
        answer += `${i}`.repeat(Math.min(xNums[i], yNums[i]));
    }
    
    if (answer === '') {
        return '-1';
    }
    
    if (answer[0] === '0') {
        return '0';
    }
    
    return answer;
}
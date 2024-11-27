const winningRate = {
    6:1,
    5:2,
    4:3,
    3:4,
    2:5,
}

function solution(lottos, win_nums) {
    var answer = [];
    let matchedCount = 0;
    let uncheckableCount = 0;
    
    for (const n of lottos) {
        if (n === 0) {
            uncheckableCount++;
            continue;
        }
        
        if (win_nums.includes(n)){
            matchedCount++;
        }
    }
    
    answer.push(winningRate[matchedCount + uncheckableCount] || 6);
    answer.push(winningRate[matchedCount] || 6);  
    
    
    return answer;
}
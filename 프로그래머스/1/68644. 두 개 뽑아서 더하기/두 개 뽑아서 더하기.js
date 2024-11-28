function solution(numbers) {
    let numSet = new Set();
    const answer = [];
    
    for (let i = 0; i < numbers.length; i++) {
        for (let j = i + 1; j < numbers.length; j++) {
            if (i !== j){
            numSet.add(numbers[i] + numbers[j]);    
            }
        }
    }
    
    numSet.forEach(e => answer.push(e));
    answer.sort((a, b) => a - b);
    
    
    
    return answer;
}
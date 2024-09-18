function solution(number) {
    let sum = 0;
    
    for (let i of number) {
        sum += Number(i);
    }
    
    return sum % 9;
}
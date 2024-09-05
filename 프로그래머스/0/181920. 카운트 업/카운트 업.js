function solution(start_num, end_num) {
    let answer = [];
    
    while(start_num <= end_num) {
        answer.push(start_num);
        start_num++;
    }
    
    return answer;
}
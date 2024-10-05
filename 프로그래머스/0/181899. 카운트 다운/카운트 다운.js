function solution(start_num, end_num) {
    var answer = [];
    
    while (end_num <= start_num) {
        answer.push(start_num);
        start_num--;
    }
    
    return answer;
}
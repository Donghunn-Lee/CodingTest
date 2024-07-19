function solution(num_str) {
    var answer = 0;
    
    for (num of num_str) {
        answer += +num
    }
    
    return answer;
}
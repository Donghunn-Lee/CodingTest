function solution(num_list) {
    var answer = 0;
    
    if (num_list.length <= 10) {
        answer = num_list.reduce((acc, cur) => acc * cur);
    } else if (11 <= num_list.length) {
        answer = num_list.reduce((acc, cur) => acc + cur);
    }
    
    return answer;
}
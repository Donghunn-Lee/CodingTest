function solution(my_string, indices) {
    var answer = '';
    
    [...my_string].forEach((val, idx) => {
        if (!indices.includes(idx)) answer += val;
    })
    
    return answer;
}
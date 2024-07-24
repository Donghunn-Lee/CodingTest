function solution(my_string) {
    var answer = [];
    var i = 0
    var tmp = '';
    let length = my_string.length;
    
    while (i < length) {
        if (my_string[i] === " ") {
            if (tmp) {
                answer.push(tmp);
                tmp = '';
            }
        } else {
            tmp += my_string[i];
            
            if (i === length - 1) {
                answer.push(tmp)
            }
        }
        i++
    }
    
    return answer;
}
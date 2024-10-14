function solution(num_list) {
    var answer = 0;
    
    for (let n of num_list) {
        while (n != 1) {
            if (n % 2 == 1) {
                n = (n - 1) / 2;
            } else {
                n /= 2;
            }
            
            answer++;
        }
    }
    
    return answer;
}
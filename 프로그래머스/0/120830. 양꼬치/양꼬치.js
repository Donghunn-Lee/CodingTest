function solution(n, k) {
    var answer = 0;
    let service = ~~(n / 10);
    
    answer = n * 12000 + (k - service) * 2000;
    
    return answer;
}
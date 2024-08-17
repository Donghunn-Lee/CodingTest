function solution(food) {
    var answer = '';
    
    for (let i = 1; i < food.length; i++) {
        let num = Math.floor(food[i] / 2);
        answer += i.toString().repeat(num);
    }
    
    return answer + '0' + [...answer].reverse().join("");
}
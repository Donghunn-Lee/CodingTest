function solution(ingredient) {
    let answer = 0;
    let hamburger = [];
    
    for (let i of ingredient) {
        hamburger.push(i)
        let n = hamburger.length;

        if (hamburger[n - 4] === 1 && hamburger[n - 3] === 2 && hamburger[n - 2] === 3 && hamburger[n - 1] === 1) {
            for (let i = 0; i < 4; i++) hamburger.pop();
            answer++;
        }


    }
    
    return answer;
}
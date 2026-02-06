function solution(people, limit) {
    let answer = 0;
    
    people.sort((a, b) => a - b);
    
    while (people.length) {
        let weightest = people.pop();
        
        if (weightest + people[0] <= limit) {
            people.shift();
        }
        
        answer++;
        
    }
    
    
    return answer;
}
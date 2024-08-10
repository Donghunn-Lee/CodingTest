function solution(today, terms, privacies) {
    let answer = [];
    
    const N = privacies.length;
    const terms_dict = {}
    
    today = today.split(".").map(Number);
    terms.map((e) => e.split(' ')).forEach((val) => terms_dict[val[0]] = +val[1]);
    privacies.forEach((val, idx, arr) => arr[idx] = val.split(" "))
    
    for (let i = 0; i < N; i++) {
        let [date, grade] = [privacies[i][0].split(".").map(Number), privacies[i][1]];
        let elapsedMonth = 0;
        
        elapsedMonth = ((today[0] - date[0]) * 12) + (today[1] - date[1]) + (today[2] - date[2] < 0 ? -1 : 0);
        
        if (terms_dict[grade] <= elapsedMonth) {
            answer.push(i + 1)
        }
    }
    
    return answer;
}
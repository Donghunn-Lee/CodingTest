function solution(name, yearning, photo) {
    let score_dict = {};
    let N = name.length, M = photo.length;
    for (let i = 0; i < N; i++) {
        score_dict[name[i]] = yearning[i];
    }
    
    let total_score = Array(M).fill(0);

    for (let i = 0; i < M; i++) {
        for (const person of photo[i]) {
            if (person in score_dict) {
                total_score[i] += score_dict[person];
            }
        }
    }
    
    return total_score;
}
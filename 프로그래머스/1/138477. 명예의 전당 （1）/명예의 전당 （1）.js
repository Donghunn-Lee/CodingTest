function bisect(arr, target) {
    let left = 0;
    let right = arr.length;

    while (left < right) {
        const mid = Math.floor((left + right) / 2);

        // arr가 내림차순 정렬되었다고 가정
        if (arr[mid] > target) { 
            left = mid + 1;
        } else {
            right = mid;
        }
    }

    return left;
}


function solution(k, score) {
    const hallOfFame = [];
    const answer = [];
    
    for (let i = 0; i < score.length; i++) {
        let idx = bisect(hallOfFame, score[i]);
        hallOfFame.splice(idx, 0, score[i]);
        
        if (k < hallOfFame.length) hallOfFame.pop();

        // hallOfFame은 내림차순으로 정렬되므로 가장 작은 값은 마지막에 위치
        answer.push(hallOfFame.at(-1));
    }
    
    return answer;
}
function solution(participant, completion) {
    const participantResult = {};
    
    participant.forEach((v, i) => {
        if (participantResult.hasOwnProperty(v)) {
            participantResult[v] += 1;
            return;
        }
        
        participantResult[v] = 1;
    })
    
    completion.forEach((v, i) => {
        if (participantResult.hasOwnProperty(v)) {
            participantResult[v] -= 1;
        }
    })
    
    for (let p in participantResult) {
        if (participantResult[p] > 0) return p;
    }
}
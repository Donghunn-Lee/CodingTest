function solution(friends, gifts) {
    let N = friends.length;
    let friends_num = {};
    let gifts_log = Array(N).fill(0).map((e) => Array(N).fill(0));
    let gifts_index = Array(N).fill(0);
    let next_month = Array(N).fill(0)
    
    // 코드 작성에 용이하도록 이름을 인덱스로 바꿔주는 딕셔너리 생성.
    for (let i = 0; i < N; i++) {
        friends_num[friends[i]] = i;
    }
    
    // 선물 로그 테이블 작성.
    for (let log of gifts) {
        log = log.split(' ');
        let A = log[0], B = log[1];
        
        gifts_log[friends_num[A]][friends_num[B]] += 1;
    }
    
    // 선물 지수 계산.
    for (let i = 0; i < N; i++) {
        for (let j = 0; j < N; j++) {
            if (i === j) continue;
            
            gifts_index[i] += gifts_log[i][j] - gifts_log[j][i]
        }
    }
    
    // 다음 달 선물 현황 계산.
    for (let i = 0; i < N; i++) {
        for (let j = i + 1; j < N; j++) {
            
            if (gifts_log[i][j] < gifts_log[j][i]) {
                next_month[j] += 1;
            } else if (gifts_log[i][j] > gifts_log[j][i]) {
                next_month[i] += 1;
            } else {
                if (gifts_index[i] < gifts_index[j]) {
                    next_month[j] += 1;
                } else if (gifts_index[i] > gifts_index[j]) {
                    next_month[i] += 1;
                }
            }
        }
    }
    
    return Math.max(...next_month);
}
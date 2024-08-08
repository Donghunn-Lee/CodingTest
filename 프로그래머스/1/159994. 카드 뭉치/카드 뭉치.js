function solution(cards1, cards2, goal) {
    var sentence = '';
    const N = cards1.length, M = cards2.length;
    let cur1 = 0, cur2 = 0;
    
    for (const word of goal) {
        if (cur1 < N && cards1[cur1] === word) {
            sentence += word;
            cur1++;
        } else if (cur2 < M && cards2[cur2] === word) {
            sentence += word;
            cur2++;
        } else {
            return 'No';
        }
    }
    
    return 'Yes';
}
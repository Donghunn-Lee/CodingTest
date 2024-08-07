function solution(keymap, targets) {
    const N = keymap.length, M = targets.length;
    let key_dict = {};
    let answer = []
    
    
    for (let i = 0; i < N; i++) {
        for (let j = 0; j < keymap[i].length; j++) {
            let cur_char = keymap[i][j];
            if (key_dict.hasOwnProperty(cur_char)) {
                key_dict[cur_char] = Math.min(key_dict[cur_char], j + 1);
            } else {
                key_dict[cur_char] = j + 1;
            }
        }
    }
    
    for (let i = 0; i < M; i++) {
        let count = 0;
        
        for (let j = 0; j < targets[i].length; j++) {
            let target = targets[i][j];
            
            if (key_dict.hasOwnProperty(target)) {
                count += key_dict[target];
            } else {
                count = -1;
                break;
            }
        }
        
        answer.push(count);
    }
    
    return answer;
}

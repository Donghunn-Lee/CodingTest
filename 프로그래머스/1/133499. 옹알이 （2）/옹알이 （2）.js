function solution(babbling) {
    var answer = 0;
    const words = ["aya", "ye", "woo", "ma"];
    const nums = ["1", "2", "3", "4"];

    for (let babble of babbling) {
        for (let i = 0; i < words.length; i++) {
            babble = babble.replaceAll(words[i], `${i + 1}`);
        }
                
        if (babble.length === 1 && nums.includes(babble)) {
            answer++;
            continue;
        }

        let flag = true;

        for (let i = 0; i < babble.length - 1; i++) {
            if (!nums.includes(babble[i]) || babble[i] === babble[i + 1]){
                flag = false;
                break;
            }
        }

        if (nums.includes(babble[babble.length - 1]))
            if (flag) answer++;
    }
    
    return answer;
}
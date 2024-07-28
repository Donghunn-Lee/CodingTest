// 그룹 단어 체커

const fs = require("fs");

function Input() {
    return fs.readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split("\n");
}

function sol() {
    let input_data = Input();
    let N = Number(input_data[0]);
    let words = input_data.slice(1);
    let ans = 0;
    
    for (word of words) {
        let last = word[0];
        let visited = new Set([last]);
        let check = true;

        for (let i = 1; i < word.length; i++) {
            if (last != word[i]) {
                if (visited.has(word[i])) {
                    check = false;
                    break;
                }
                
                last = word[i];
                visited.add(last);
                
            }
        }

        if (check) {
            ans += 1;
        }

    }
    
    console.log(ans);
    
}

sol();
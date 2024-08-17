// 극장 좌석

const fs = require("fs");
const input = fs.readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt").toString().trim().split("\n").map(Number);

function sol() {
    const N = input[0];
    const M = input[1];
    const vip = input.slice(2);
    const seats = Array(N + 1).fill(0);
    const dp = Array(N + 1).fill(0);
    let answer = 1;

    for (let i of vip) {
        seats[i] = 1
    }

    dp[1] = 1;
    dp[2] = 2;
    
    for (let i = 3; i <= N; i++) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }

    let cnt = 0;

    for (let i = 1; i <= N; i++) {
        if (!seats[i]) {
            cnt++;
        } else if (cnt){
            answer *= dp[cnt];
            cnt = 0
        }
    }

    if (cnt) {
        answer *= dp[cnt];
    }

    return answer;
}

console.log(sol());
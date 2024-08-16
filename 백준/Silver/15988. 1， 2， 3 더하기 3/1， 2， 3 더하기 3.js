// 1, 2, 3 더하기 3

const fs = require("fs");
const input = fs.readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt").toString().trim().split("\n").map(Number);


function sol() {
    const T = input[0];
    const answer = [];
    const dp = Array(Math.max(...input.slice(1)) + 1).fill(0);
    dp[1] = 1;
    dp[2] = 2;
    dp[3] = 4;

    for (let i = 4; i < dp.length; i++) {
        for (let k = 1; k <= 3; k++) {
            dp[i] = (dp[i - k] + dp[i]) % 1_000_000_009;
        }
    }

    for (let i = 1; i <= T; i++) {
        answer.push(dp[input[i]] % 1_000_000_009);
    }

    return answer.join("\n");
}

console.log(sol());
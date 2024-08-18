// 퇴사 2

const fs = require("fs");
const input = fs.readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt").toString().trim().split("\n");

function sol() {
    const N = +input[0];
    const T = [], P = [];
    const dp = Array(N + 1).fill(0);

    for (let i = 1; i <= N; i++) {
        let e = input[i].split(" ").map(Number);
        T.push(e[0]);
        P.push(e[1]);
    }

    for (let i = 0; i < N; i++) {
        if (0 < i) {
            dp[i] = Math.max(dp[i], dp[i - 1]);
        }

        if (dp[i + T[i]] !== undefined){
            dp[i + T[i]] = Math.max(dp[i + T[i]], dp[i] + P[i])
        }

    }

    return Math.max(...dp);
}

console.log(sol());
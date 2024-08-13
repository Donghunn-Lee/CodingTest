// 2차원 배열의 합

const fs = require("fs");
const input = fs.readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
    .toString().trim().split("\n");



function sol() {
    const [N, M] = input.shift().split(" ").map(Number);
    const arr = input.slice(0, N).map(e => e.split(" ").map(Number));
    const K = +input[N];
    const area = input.slice(N + 1);
    const answer = [];

    for (let k = 0; k < K; k++) {
        const [y1, x1, y2, x2] = area[k].split(" ").map(Number);
        let sum = 0;

        for (let i = y1; i <= y2; i++) {
            for (let j = x1; j <= x2; j++) {
                sum += arr[i - 1][j - 1];
            }
        }

        answer.push(sum);
    }

    return answer.join("\n");
}

console.log(sol());

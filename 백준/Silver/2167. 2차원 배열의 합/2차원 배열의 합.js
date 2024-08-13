// 2차원 배열의 합

const fs = require("fs");
const input = fs.readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
    .toString().trim().split("\n");



function sol() {
    const [N, M] = input[0].split(" ").map(Number);
    const arr = input.slice(1, N + 1).map(e => e.split(" ").map(Number));
    const areas = input.slice(N + 2).map(e => e.split(" ").map(Number));
    const sum = Array(N + 1).fill().map(_ => Array(M + 1).fill(0));
    const answer = [];

    for (let i = 0; i < N; i++) {
        sum[i + 1][1] = sum[i][1] + arr[i][0];
        
    }

    for (let j = 0; j < M; j++) {
        sum[1][j + 1] = sum[1][j] + arr[0][j];
    }

    for (let i = 2; i <= N; i++) {
        for (let j = 2; j <= M; j++) {
            sum[i][j] = arr[i - 1][j - 1] + sum[i - 1][j] + sum[i][j - 1] - sum[i - 1][j - 1];
        }
    }


    for (let area of areas) {
        const [si, sj, ei, ej] = area;
        answer.push(sum[ei][ej] - sum[si-1][ej] - sum[ei][sj-1] + sum[si-1][sj-1]);
    }


    return answer.join("\n");
}

console.log(sol());

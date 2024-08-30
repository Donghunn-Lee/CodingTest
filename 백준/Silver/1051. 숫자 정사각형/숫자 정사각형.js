// 숫자 정사각형

const fs = require("fs");
const input = fs.readFileSync(process.platform === "linux" ? "/dev/stdin" : "input.txt").toString().trim().split("\n");

const [N, M] = input[0].split(" ").map(Number);
const square = input.slice(1).map(e => e.split("").map(Number));

function sol() {
    const length = Math.max(N, M);
    for (let k = length - 1; 0 <= k; k--) {
        for (let i = 0; i < N; i++) {
            for (let j = 0; j < M; j++) {
                if (i + k < N && j + k < M) {
                    if (square[i][j] === square[i + k][j] && square[i + k][j] === square[i + k][j + k] && square[i][j] === square[i][j + k]) {
                        return (k + 1) ** 2
                    }
                }
            }
        }

    }
}

console.log(sol());
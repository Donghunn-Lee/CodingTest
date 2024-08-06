// 숫자 카드
const fs = require("fs");

function Input() {
    return fs.readFileSync(process.platform === "linux" ? "/dev/stdin" : "./baekjoon/JS/input.txt")
    .toString()
    .trim()
    .split("\n")
    .map((e) => e.split(" ").map(Number));
}

function sol() {
    const input = Input();
    const N = input[0][0];
    const cards = new Set(input[1]);
    const M = input[2][0];
    const target = input[3];
    let answer = Array(M).fill(0);

    for (let i = 0; i < M; i++) {
        if (cards.has(target[i])) {
            answer[i] = 1;
        } else {
            answer[i] = 0;
        }
    }
    
    return answer.join(" ");
}

console.log(sol());
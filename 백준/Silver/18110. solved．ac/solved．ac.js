// solved.ac

const fs = require("fs");

function Input() {
    return fs.readFileSync(process.platform === "linux" ? "/dev/stdin" : "./baekjoon/JS/input.txt")
    .toString()
    .trim()
    .split("\n")
    .map(Number);
}

function sol() {
    let input_data = Input();
    let N = input_data.shift();

    if (N == 0) {
        console.log(0);
        process.exit();
    }

    let cut = Math.round(N * 0.15);
    input_data = input_data.sort((a, b) => a - b).slice(cut, N - cut);

    return Math.round(input_data.reduce((acc, cur) => acc + cur, 0) / (N - cut * 2));
}

console.log(sol());
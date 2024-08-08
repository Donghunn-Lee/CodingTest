// 회사에 있는 사람

const fs = require("fs");

function Input() {
    return fs.readFileSync(process.platform === "linux" ? "/dev/stdin" : "./baekjoon/JS/input.txt")
    .toString()
    .trim()
    .split("\n")
}

function sol() {
    const inputData = Input();
    const N = inputData.shift();
    const log = inputData.map((e) => e.split(" ").map((e) => e.trim()));
    const inCompany = new Set();

    for (let i = 0; i < N; i++) {
        if (log[i][1] === 'enter') {
            inCompany.add(log[i][0]);
        } else {
            inCompany.delete(log[i][0]);
        }
    }

    return [...inCompany].sort((a, b) => {
        if (a < b) {
            return 1;
        } else {
            return -1;
        }
    }).join("\n");
}

console.log(sol());
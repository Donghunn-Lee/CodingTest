// 설탕 배달

const fs = require("fs");

let N = Number(fs.readFileSync(process.platform === "linux" ?
    "/dev/stdin" : "./baekjoon/JS/input.txt").toString().trim())

function sol() {
    let n_five = Math.floor(N / 5);
    let n_three;
    
    for(let i = n_five; 0 <= i; i--) {
        if ((N - i * 5) % 3 === 0) {
            return i + (N - i * 5) / 3;
        }
    }

    return -1;
}

console.log(sol());
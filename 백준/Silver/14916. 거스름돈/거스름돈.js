// 거스름돈

const fs = require("fs");
const input = +fs
  .readFileSync(
    process.platform === "linux" ? "/dev/stdin" : "./baekjoon/JS/input.txt"
  )
  .toString()
  .trim();

function sol() {
    let N = input;

    if (N === 1 || N === 3) {
        return -1;
    }

    let answer = Math.floor(N / 5);
    let remainder = N % 5;

    if (remainder % 2 === 0) {
        answer += remainder / 2;
    } else {
        answer += (-1) + (remainder + 5) / 2;
    }

    return answer;
}

console.log(sol())

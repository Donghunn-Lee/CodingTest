// 줄세우기

const fs = require("fs");
const input = fs.readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt").toString().trim().split("\n").map(e => e.split(" ").map(Number));

const P = +input[0];

function bisect(arr, target) {
    let left = 0;
    let right = arr.length;

    while (left < right) {
        const mid = Math.floor((left + right) / 2);

        if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }

    return left;
}

function sol(n) {
    const arr = [];
    let count = 0;

    for (let i = 1; i <= 20; i++) {
        let stdNum = input[n][i];
        const idx = bisect(arr, stdNum);
        arr.splice(idx, 0, stdNum);
        count += arr.length - 1 - idx;
    }

    return count;
}

function main() {
    let answer = [];

    for (let i = 1; i <= P; i++) {
        answer.push(`${i} ${sol(i)}`);
    }

    console.log(answer.join("\n"));
}

main();
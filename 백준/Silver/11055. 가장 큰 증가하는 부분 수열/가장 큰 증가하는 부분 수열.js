// 가장 큰 증가하는 부분 수열

const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

function bisectLeft(arr, target) {
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

function sol() {
    const N = +input[0];
    const A = input[1].split(" ").map(Number);
    const dp = [];

    for (let i = 0; i < N; i++ ) {
        dp[i] = A[i];

        for (let j = 0; j < i; j++) {
            if (A[j] < A[i] && dp[i] < dp[j] + A[i]) {
                dp[i] = dp[j] + A[i];
            }
        }
    }

    return Math.max(...dp);
}

console.log(sol());
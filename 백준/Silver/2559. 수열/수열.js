// 수열

const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "input.txt")
  .toString()
  .trim()
  .split("\n");

function main() {
  const [N, K] = input[0].split(" ").map(Number);
  const seq = input[1].split(" ").map(Number);
  const prefixSum = [0];
  let ans = Number.MIN_SAFE_INTEGER;

  for (let i = 1; i <= N; i++) {
    prefixSum[i] = prefixSum[i - 1] + seq[i - 1];
  }

  for (let i = K; i <= N; i++) {
    ans = Math.max(ans, prefixSum[i] - prefixSum[i - K]);
  }

  console.log(ans);
}

main();

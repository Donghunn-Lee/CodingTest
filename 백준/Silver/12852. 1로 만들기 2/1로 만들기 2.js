// 1로 만들기 2

const fs = require("fs");
const X = +fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim();

function sol() {
  const dp = [0, 0, 1, 1];
  const operation = [0, 0, 1, 1];
  const answer = [];

  for (let i = 4; i <= X; i++) {
    let nxt1 = i % 3 === 0 ? operation[i / 3] + 1 : Infinity;
    let nxt2 = i % 2 === 0 ? operation[i / 2] + 1 : Infinity;
    let nxt3 = operation[i - 1] + 1;

    if (nxt1 <= nxt2 && nxt1 <= nxt3) {
      operation.push(nxt1);
      dp.push(i / 3);
    } else if (nxt2 <= nxt1 && nxt2 <= nxt3) {
      operation.push(nxt2);
      dp.push(i / 2);
    } else if (nxt3 <= nxt1 && nxt3 <= nxt2) {
      operation.push(nxt3);
      dp.push(i - 1);
    }
  }

  let cur = X;

  while (1 <= cur) {
    answer.push(cur);
    cur = dp[cur];
  }

  return `${answer.length - 1}\n${answer.join(" ")}`;

}

console.log(sol());

const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const N = +input;

const dp = (num) => {
  const memo = [0, 1, 0, 1, 1];

  for (let i = 5; i <= num; i++) {
    // 하나라도 0이면 다음에 상근이가 이기는 거니까 1
    if (memo[i - 1] + memo[i - 3] + memo[i - 4] < 3) memo[i] = 1;
    // 전부 1이면 무조건 횟수 2번이므로 창영이가 이김. 따라서 0
    else memo[i] = 0;
  }

  return memo[num] === 1 ? "SK" : "CY";
};

console.log(dp(N));
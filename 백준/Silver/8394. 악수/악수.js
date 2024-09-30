// 피보나치 수의 확장

const fs = require("fs");
const N = +fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "input.txt")
  .toString()
  .trim();

function main() {
  let [dp_1, dp_2, dp_3] = [1, 2, 3];

    if (N === 1) {
        console.log(dp_1);
        return;
    } else if (N === 2) {
        console.log(dp_2);
        return
    }

  for (let i = 4; i <= N; i++) {
    [dp_1, dp_2, dp_3] = [dp_2, dp_3, (dp_2 + dp_3) % 10];
  }

  console.log(dp_3);
}

main();

// 분해합

const fs = require("fs");

function Input() {
  return Number(
    fs
      .readFileSync(
        process.platform === "linux" ? "/dev/stdin" : "./baekjoon/JS/input.txt"
      )
      .toString()
  );
}

function sol() {
  let N = Input();

  for (let i = 0; i < N; i++) {
    var sum = i;

    for (j of i.toString()) {
      sum += Number(j);
    }

    if (sum === N) {
        console.log(i);
        return;
    }
  }

  console.log(0);
}

sol();
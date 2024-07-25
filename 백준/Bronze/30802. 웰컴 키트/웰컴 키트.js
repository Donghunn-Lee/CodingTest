// 웰컴 키트

const fs = require("fs");

function Input() {
  return fs
    .readFileSync(
      process.platform == "linux" ? "/dev/stdin" : "./baekjoon/JS/input.txt"
    )
    .toString()
    .trim()
    .split("\n");
}

function sol() {
    let input_data = Input();
    let N = Number(input_data[0]);
    let sizes = input_data[1].split(" ").map(Number);
    let T_P = input_data[2].split(" ").map(Number);
    var answer = [];

    let tmp = 0;
    for (i of sizes) {
        tmp += Math.ceil(i / T_P[0]);
    }

    answer.push(tmp);
    answer.push(`${Math.floor(N / T_P[1])} ${N % T_P[1]}`);
    
    console.log(answer.join("\n"));
}

sol();
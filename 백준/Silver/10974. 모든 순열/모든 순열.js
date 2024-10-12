const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const N = Number(input);

let visited = Array(N).fill(false);

let selected = Array(N).fill(0);

let answer = "";

function dfs(depth) {
  if (depth === N) {
    let result = [];
    for (let i = 0; i < N; i++) {
      result.push(selected[i]);
    }

    answer += result.join(" ") + "\n";
  }

  for (let i = 1; i <= N; i++) {
    if (visited[i]) {
      continue;
    }

    selected[depth] = i;
    visited[i] = true;
    dfs(depth + 1);
    visited[i] = false;
  }
}

dfs(0);

console.log(answer.trim());
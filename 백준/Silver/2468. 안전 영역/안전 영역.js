const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = require("fs")
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n");

const N = +input.shift();
const area = input.map((e) => e.split(" ").map(Number));

function findSafeArea(rain) {
  const graph = input.map((e) => e.split(" ").map(Number));
  const visited = Array.from(Array(N), () => Array(N).fill(false));
  const dir = [
    [1, 0],
    [0, 1],
    [-1, 0],
    [0, -1],
  ];
  let safeArea = 0;

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      if (rain < graph[i][j]) graph[i][j] = 1;
      else graph[i][j] = 0;
    }
  }

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      if (graph[i][j] == 1 && !visited[i][j]) {
        dfs(i, j);
        safeArea++;
      }
    }
  }

  function dfs(ci, cj) {
    if (isValidRange(ci, cj) && !visited[ci][cj] && graph[ci][cj] === 1) {
      visited[ci][cj] = true;

      for (let d of dir) {
        const [nx, ny] = [ci + d[0], cj + d[1]];
        dfs(nx, ny);
      }
    }
  }

  function isValidRange(i, j) {
    if (i < 0 || i >= N || j < 0 || j >= N) return false;
    else return true;
  }

  return safeArea;
}

function main() {
  let MAX = 0;
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      MAX = Math.max(MAX, area[i][j]);
    }
  }

  let answer = 1;
  for (let rain = 0; rain <= MAX; rain++) {
    answer = Math.max(answer, findSafeArea(rain));
  }

  console.log(answer);
}

main();

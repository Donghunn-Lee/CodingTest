// 뱀

const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

function sol() {
  const N = +input.shift();
  const K = +input.shift();
  const board = Array(N + 1)
    .fill()
    .map(() => Array(N + 1).fill(0));
  board[1][1] = 1;
  const apples = input.slice(0, K).map((e) => e.split(" ").map(Number));
  const L = +input.shift();
  const directionChange = {};
  input
    .slice(K)
    .map((e) => e.split(" "))
    .forEach((e) => (directionChange[+e[0]] = e[1]));

  const snake = [[1, 1]];
  const di = [0, 1, 0, -1];
  const dj = [1, 0, -1, 0];
  let direction = 0;
  let time = 0;

  for (const apple of apples) {
    board[apple[0]][apple[1]] = "a";
  }

  while (true) {
    time++;

    const head = snake.at(-1);
    let ni = head[0] + di[direction];
    let nj = head[1] + dj[direction];

    if (1 <= ni && ni <= N && 1 <= nj && nj <= N && board[ni][nj] !== 1) {
      snake.push([ni, nj]);

      if (board[ni][nj] !== "a") {
        let tail = snake.shift();
        board[tail[0]][tail[1]] = 0;
      }

      board[ni][nj] = 1;
    } else {
      return time;
    }

    if (directionChange[time]) {
      if (directionChange[time] == "D") {
        direction = (direction + 1) % 4;
      } else {
        direction = direction - 1 < 0 ? 4 - direction - 1 : direction - 1;
      }
    }
  }
}

console.log(sol());
// 킹

const fs = require("fs");
const input = fs
  .readFileSync(process.platform == "linux" ? "/dev/stdin" : "input.txt")
  .toString()
  .trim()
  .split("\n");

function main() {
  let [king, stone, N] = input.shift().split(" ");
  let [cj, ci] = [king[0].charCodeAt() % 65, king[1] - 1];
  let [sj, si] = [stone[0].charCodeAt() % 65, stone[1] - 1];
  let cmds = input;
  const direction = {
    R: [0, 1],
    L: [0, -1],
    B: [-1, 0],
    T: [1, 0],
    RT: [1, 1],
    LT: [1, -1],
    RB: [-1, 1],
    LB: [-1, -1],
  };

  for (const cmd of cmds) {
    let [di, dj] = direction[cmd.trim()];
    let [ni, nj] = [ci + di, cj + dj];

    if (0 <= ni && ni < 8 && 0 <= nj && nj < 8) {
      if (ni == si && nj == sj) {
        let [nsi, nsj] = [si + di, sj + dj];

        if (0 <= nsi && nsi < 8 && 0 <= nsj && nsj < 8) {
            si = nsi;
            sj = nsj;
        } else continue;
      }

      ci = ni;
      cj = nj;
    }
  }

  console.log(String.fromCharCode(cj + 65) + '' + (ci + 1));
  console.log(String.fromCharCode(sj + 65) + '' + (si + 1));
}

main();

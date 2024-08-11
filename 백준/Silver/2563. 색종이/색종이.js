// 색종이

const fs = require("fs");

const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

function sol() {
    const N = +input.shift();
    const colorPapers = input.map((e) => e.split(" ").map(Number));
    const covered = new Set();

    for (const colorPaper of colorPapers) {
        const marginLeft = colorPaper[0];
        const marginBottom = 100 - colorPaper[1];
        
        for (let i = marginLeft; i < marginLeft + 10; i++) {
            for (let j = marginBottom - 10; j < marginBottom; j++){
                covered.add([i, j].join(" "));
            }
        }
    }

    return covered.size;
}

console.log(sol());
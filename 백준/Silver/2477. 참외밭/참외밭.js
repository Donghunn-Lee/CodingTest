// 참외밭

const fs = require("fs");

const input = fs
  .readFileSync(
    process.platform === "linux" ? "/dev/stdin" : "./baekjoon/JS/input.txt"
  )
  .toString()
  .trim()
  .split("\n");

const N = Number(input[0]);
const sides = input.slice(1).map((e) => e.split(" ").map(Number));
let visited = {};
const longSides = [];
const dintSides = [];


for (const side of sides) {
     if (!visited[side[0]]) {
        visited[side[0]] = side;
     } else {
        delete visited[side[0]];
     }
}

for (const side in visited) {
    longSides.push(visited[side][1])
    
    const idx = sides.indexOf(visited[side]);
    dintSides.push(sides[(idx + 3) % 6][1]);
}

console.log((longSides[0] * longSides[1] - dintSides[0] * dintSides[1]) * N);

const fs = require('fs');
let [T, ...input] = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');

T = Number(T.trim());

let index = 0;
for (let i = 0; i < T; i++) {
  let count = 0;
  let N = Number(input[index++].trim());
  let sequence = [null, ...input[index++].trim().split(' ').map(Number)];
  let visited = new Array(N).fill(false);

  function DFS(node) {
    visited[node] = true;
    if (!visited[sequence[node]]) DFS(sequence[node]);
  }

  for (let k = 1; k <= N; k++) {
    if (!visited[k]) {
      DFS(k);
      count++;
    }
  }
  console.log(count);
}
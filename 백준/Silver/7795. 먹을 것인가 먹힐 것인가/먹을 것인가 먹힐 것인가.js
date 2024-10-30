const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : 'Wiki\\input.txt';
const [head, ...tail] = fs.readFileSync(path).toString().trim().split('\n');

for (let i = 0; i < Number(head); i++) {
  let cnt = 0;
  const sizeA = tail[1 + i * 3]
    .split(' ')
    .map((it) => Number(it))
    .sort((a, b) => b - a);

  const sizeB = tail[2 + i * 3]
    .split(' ')
    .map((it) => Number(it))
    .sort((a, b) => b - a);

  for (const target of sizeA) {
    for (let j = 0; j < sizeB.length; j++) {
      if (target > sizeB[j]) {
        cnt += sizeB.length - j;
        break;
      }
    }
  }
  console.log(cnt);
}
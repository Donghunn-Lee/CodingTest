// 등수 매기기

const filePath = process.platform === 'linux' ? '/dev/stdin' : 'input.txt';
const input = require('fs')
  .readFileSync(filePath)
  .toString()
  .trim()
  .split('\n');

const N = +input.shift();
const espectedRank = input.map(Number);

function main() {
    let ans = 0;

    espectedRank.sort((a, b)=> a - b);

    for (let i = 0; i < N; i++) {
        ans += Math.abs(espectedRank[i] - (i + 1));
    }

    console.log(ans)
}

main();
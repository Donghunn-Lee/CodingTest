const filePath = process.platform === 'linux' ? '/dev/stdin' : 'input.txt';
const input = require('fs')
  .readFileSync(filePath)
  .toString()
  .trim()
  .split('\n');

const [N, M] = input.shift().split(' ').map(Number);
const office = input.map((e) => e.split(' ').map(Number));
const dx = [0, 1, 0, -1];  // 동, 남, 서, 북
const dy = [1, 0, -1, 0];
const dirForCCTVType = [[], [ [0], [1], [2], [3] ], [ [0, 2], [1, 3] ], [ [0, 3], [3, 2], [2, 1], [1, 0] ], [ [0, 1, 3], [0, 1, 2], [1, 2, 3], [0, 2, 3] ], [ [0, 1, 2, 3] ]];
let minBlindSpots = Infinity;

const countBlindSpots = (graph) => {
  let count = 0;
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      if (graph[i][j] === 0) {
        count++;
      }
    }
  }
  return count;
};

const findCCTV = () => {
  const cctvInfo = [];
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      if (1 <= office[i][j] && office[i][j] < 6) {
        cctvInfo.push([i, j, office[i][j]]);
      }
    }
  }
  return cctvInfo;
};

const makeMoniteredArea = (graph, dir, ci, cj) => {
  let [ni, nj] = [ci, cj];
  while (true) {
    [ni, nj] = [ni + dy[dir], nj + dx[dir]];
    if (0 <= ni && ni < N && 0 <= nj && nj < M && graph[ni][nj] !== 6) {
      if (graph[ni][nj] === 0) graph[ni][nj] = -1;
    } else {
      break;
    }
  }
};

const dfs = (currentOffice, cctvNum, cctvInfo) => {
  if (cctvNum === cctvInfo.length) {
    minBlindSpots = Math.min(minBlindSpots, countBlindSpots(currentOffice));
    return;
  }

  const [ci, cj, cctvType] = cctvInfo[cctvNum];

  for (const dirs of dirForCCTVType[cctvType]) {
    const nextOffice = currentOffice.map((e) => [...e]);
    for (const d of dirs) {
      makeMoniteredArea(nextOffice, d, ci, cj);
    }
    dfs(nextOffice, cctvNum + 1, cctvInfo);
  }
};

function main() {
  const cctvInfo = findCCTV();
  dfs(office, 0, cctvInfo);
  console.log(minBlindSpots);
}

main();

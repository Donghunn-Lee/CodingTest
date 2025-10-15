function solution(maps) {
  const n = maps.length;
  const m = maps[0].length;

  let si = -1, sj = -1;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (maps[i][j] === 'S') { si = i; sj = j; }
    }
  }

  const DIRS = [[1,0],[0,1],[-1,0],[0,-1]];
  // visited[i][j][0 or 1]: 레버 미보유/보유 상태로 (i,j) 방문 여부
  const visited = Array.from({ length: n }, () =>
    Array.from({ length: m }, () => [false, false])
  );

  // 큐: [i, j, elapsed, hasLever]
  const q = [[si, sj, 0, 0]];
  visited[si][sj][0] = true;
  let head = 0; // shift() 대신 포인터로 O(1)

  while (head < q.length) {
    const [ci, cj, t, hasLever] = q[head++];

    // 출구 도착 & 레버를 이미 당겼다면 최단 거리
    if (maps[ci][cj] === 'E' && hasLever === 1) return t;

    for (const [di, dj] of DIRS) {
      const ni = ci + di, nj = cj + dj;
      if (ni < 0 || ni >= n || nj < 0 || nj >= m) continue;
      if (maps[ni][nj] === 'X') continue; // 벽

      // 레버 칸을 지나면 상태 전이
      const nextHas = hasLever || (maps[ni][nj] === 'L') ? 1 : 0;
      if (!visited[ni][nj][nextHas]) {
        visited[ni][nj][nextHas] = true;
        q.push([ni, nj, t + 1, nextHas]);
      }
    }
  }

  return -1; // 도달 불가
}
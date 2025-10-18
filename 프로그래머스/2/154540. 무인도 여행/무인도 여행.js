function solution(maps) {
  const n = maps.length,
    m = maps[0].length;
  let islands = [];
  const visited = Array.from(Array(n), () => Array(m).fill(0));
  const DIRS = [
    [1, 0],
    [0, 1],
    [-1, 0],
    [0, -1],
  ];

  function bfs(si, sj) {
    let meals = +maps[si][sj];
    visited[si][sj] = 1;
    const q = [[si, sj]];

    let head = 0;
    while (head < q.length) {
      const [ci, cj] = q[head++];

      for (const [di, dj] of DIRS) {
        const [ni, nj] = [ci + di, cj + dj];

        if (
          0 <= ni &&
          ni < n &&
          0 <= nj &&
          nj < m &&
          !visited[ni][nj] &&
          maps[ni][nj] !== 'X'
        ) {
          meals += +maps[ni][nj];
          visited[ni][nj] = 1;
          q.push([ni, nj]);
        }
      }
    }

    return meals;
  }

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (maps[i][j] !== 'X' && !visited[i][j]) {
        islands.push(bfs(i, j));
      }
    }
  }

  islands.sort((a, b) => a - b);

  return islands.length ? islands : [-1];
}
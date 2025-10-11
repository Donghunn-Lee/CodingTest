const findStart = (board) => {
  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board[0].length; j++) {
      if (board[i][j] === 'R') {
        return [i, j];
      }
    }
  }
  return [];
};

const solution = (board) => {
  const [n, m] = [board.length, board[0].length];
  const [si, sj] = findStart(board);
  const dir = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0],
  ];
  const visited = Array.from(Array(n), () => Array(m).fill(0));
  visited[si][sj] = 0;

  const q = [];
  q.push([si, sj, 0]);

  while (q.length > 0) {
    const [ci, cj, s] = q.shift();

    for (const [di, dj] of dir) {
      let [ni, nj] = [ci + di, cj + dj];

      while (0 <= ni && ni < n && 0 <= nj && nj < m && board[ni][nj] !== 'D') {
        [ni, nj] = [ni + di, nj + dj];
      }

      [ni, nj] = [ni - di, nj - dj];

      if (visited[ni][nj] === 0) {
        if (board[ni][nj] === 'G') {
          return s + 1;
        }

        visited[ni][nj] = 1;
        q.push([ni, nj, s + 1]);
      }
    }
  }

  return -1;
};
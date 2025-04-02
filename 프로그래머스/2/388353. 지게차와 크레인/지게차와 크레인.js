function solution(storage, requests) {
  const [h, w] = [storage.length, storage[0].length];
  let result = h * w;
  const storageMap = storage.map((v) => v.split(''));
  const dir = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0],
  ];

  const isOnBoundary = (i, j) => {
    if (i < 0 || h <= i || j < 0 || w <= j) {
      return true;
    }

    return false;
  };

  const useFolkLift = (si, sj, arr) => {
    const visited = Array.from(Array(h), () => Array(w).fill(false));
    const q = [[si, sj]];
    visited[si][sj] = true;

    while (q.length) {
      const [ci, cj] = q.shift();

      for (const [di, dj] of dir) {
        const [ni, nj] = [ci + di, cj + dj];

        if (isOnBoundary(ni, nj)) {
          storageMap[si][sj] = '';

          return true;
        }

        if (!visited[ni][nj] && arr[ni][nj] === '') {
          visited[ni][nj] = true;
          q.push([ni, nj]);
        }
      }
    }

    return false;
  };

  const useCrane = (req) => {
    for (let i = 0; i < h; i++) {
      for (let j = 0; j < w; j++) {
        if (storageMap[i][j] === req) {
          storageMap[i][j] = '';
          result--;
        }
      }
    }
  };

  requests.forEach((request) => {
    const currentStorage = JSON.parse(JSON.stringify(storageMap));

    if (request.length == 2) {
      useCrane(request[0]);
    } else {
      for (let i = 0; i < h; i++) {
        for (let j = 0; j < w; j++) {
          if (storageMap[i][j] === request) {
            if (useFolkLift(i, j, currentStorage)) {
              result--;
            }
          }
        }
      }
    }
  });

  return result;
}
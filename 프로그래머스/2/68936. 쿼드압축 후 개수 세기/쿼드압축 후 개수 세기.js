function solution(arr) {
  const n = arr.length;
  const answer = [0, 0];

  function compress(r, c, size) {
    const first = arr[r][c];
    let same = true;

    for (let i = r; i < r + size && same; i++) {
      for (let j = c; j < c + size; j++) {
        if (arr[i][j] !== first) {
          same = false;
          break;
        }
      }
    }

    if (same) {
      answer[first] += 1;
      return;
    }

    const half = size >> 1;
    compress(r, c, half);
    compress(r, c + half, half);
    compress(r + half, c, half);
    compress(r + half, c + half, half);
  }

  compress(0, 0, n);
  return answer;
}
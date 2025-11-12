function solution(n, info) {
  let maxDiff = -Infinity;
  let maxDist = null;
  const cur = Array(11).fill(0);

  function better(a, b) {
    if (!b) return true;
    for (let i = 10; i >= 0; i--) {
      if (a[i] !== b[i]) return a[i] > b[i];
    }
    return false;
  }

  function dfs(i, arrows, diff) {
    if (i === 10) {
      cur[10] = arrows;
      if (diff > maxDiff || (diff === maxDiff && better(cur, maxDist))) {
        maxDiff = diff;
        maxDist = [...cur];
      }
      cur[10] = 0;
        return;
    }

    const score = 10 - i;
    const need = info[i] + 1;

    if (arrows >= need) {
      cur[i] = need;
      dfs(i + 1, arrows - need, diff + score);
      cur[i] = 0;
    }

    const lose = info[i] > 0 ? -score : 0;
    dfs(i + 1, arrows, diff + lose);
  }

  dfs(0, n, 0);

  return maxDiff <= 0 ? [-1] : maxDist;
}

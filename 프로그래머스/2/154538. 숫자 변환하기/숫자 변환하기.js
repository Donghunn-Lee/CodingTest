function solution(x, y, n) {
  if (x === y) return 0;
  if (x > y) return -1;

  const dist = Array(y + 1).fill(-1);
  const q = [x];
  dist[x] = 0;

  for (let i = 0; i < q.length; i++) {
    const v = q[i];
    const nexts = [v + n, v * 2, v * 3];

    for (const nv of nexts) {
      if (nv > y) continue;
      if (dist[nv] !== -1) continue;
      dist[nv] = dist[v] + 1;
      if (nv === y) return dist[nv];
      q.push(nv);
    }
  }
  return -1;
}
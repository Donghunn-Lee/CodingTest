function solution(relation) {
  const n = relation.length;
  const m = relation[0].length;
  const combinations = [];

  function dfs(idx, bucket) {
    if (bucket.length > 0) {
      combinations.push([...bucket]);
    }

    for (let i = idx; i < m; i++) {
      bucket.push(i);
      dfs(i + 1, bucket);
      bucket.pop();
    }
  }

  dfs(0, []);

  combinations.sort((a, b) => a.length - b.length);

  const candidates = [];

  for (const comb of combinations) {
    const isMinimal = candidates.every(
      (key) => !key.every((k) => comb.includes(k))
    );

    if (!isMinimal) continue;

    const set = new Set();
    for (let i = 0; i < n; i++) {
      const key = comb.map((idx) => relation[i][idx]).join('|');
      set.add(key);
    }

    if (set.size === n) {
      candidates.push(comb);
    }
  }

  return candidates.length;
}

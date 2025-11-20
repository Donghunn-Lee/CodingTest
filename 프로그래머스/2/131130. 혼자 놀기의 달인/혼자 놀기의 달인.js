function solution(cards) {
  let n = cards.length;
  let checked = Array(n).fill(false);
  const groups = [];

  function dfs(s, c) {
    checked[s] = true;
    let next = cards[s] - 1;

    if (!checked[next]) {
      return dfs(next, c + 1);
    }

    return c;
  }

  for (let i = 0; i < n; i++) {
    if (!checked[i]) {
      groups.push(dfs(i, 1));
    }
  }

  if (groups.length < 2) return 0;

  groups.sort((a, b) => b - a);

  return groups[0] * groups[1];
}
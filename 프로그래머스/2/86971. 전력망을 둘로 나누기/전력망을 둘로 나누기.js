function solution(n, wires) {
  let answer = Infinity;

  const graph = Array.from(Array(n + 1), () => Array());

  for (const [v1, v2] of wires) {
    graph[v1].push(v2);
    graph[v2].push(v1);
  }

  function dfs(s, ban, graph, visited, count) {
    for (const nv of graph[s]) {
      if (!visited[nv] && nv !== ban) {
        visited[nv] = 1;
        dfs(nv, ban, graph, visited, count + 1);
      }
    }
  }

  for (const [v1, v2] of wires) {
    const visited1 = Array(n + 1).fill(0);
    const visited2 = Array(n + 1).fill(0);

    visited1[v1] = 1;
    visited2[v2] = 1;

    dfs(v1, v2, graph, visited1, 1);
    dfs(v2, v1, graph, visited2, 1);

    answer = Math.min(answer, Math.abs(visited1.reduce((acc, cur) => acc + cur, 0) - visited2.reduce((acc, cur) => acc + cur, 0)));
  }

  return answer;
}
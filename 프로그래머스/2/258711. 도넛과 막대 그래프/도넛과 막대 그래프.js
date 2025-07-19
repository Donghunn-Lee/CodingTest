function solution(edges) {
  const answer = [0, 0, 0, 0];
  const graph = {};

  for (const edge of edges) {
    if (!graph[edge[0]]) graph[edge[0]] = [0, 0];
    if (!graph[edge[1]]) graph[edge[1]] = [0, 0];
  }

  for (const edge of edges) {
    graph[edge[0]][0]++;
    graph[edge[1]][1]++;
  }

  for (const node in graph) {
    // 정점
    if (2 <= graph[node][0] && graph[node][1] == 0) {
      answer[0] = +node;
    }

    // 막대
    if (graph[node][0] == 0 && 1 <= graph[node][1]) {
      answer[2]++;
    }

    // 8자
    if (graph[node][0] == 2 && 2 <= graph[node][1]) {
      answer[3]++;
      continue;
    }
  }

  answer[1] = graph[answer[0]][0] - (answer[2] + answer[3]);

  return answer;
}
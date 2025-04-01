function solution(players, m, k) {
  var answer = 0;
  const server = Array(29).fill(0);

  for (let i = 0; i < 24; i++) {
    const l = Math.floor(players[i] / m)
    const lack = l - (server[i]);

    if (0 < lack) {
      for (let j = 0; j < k; j++) {
        server[i + j] += lack;
      }

      answer += lack;
    }
  }

  return answer;
}
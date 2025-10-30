function solution(k, tangerine) {
  let answer = 0;
  const count = [];
  tangerine.forEach((e) => {
    count[e] = count[e] ? count[e] + 1 : 1;
  });
  count.sort((a, b) => b - a);

  let i = 0;
  while (k > 0) {
    if (count[i] >= k) {
      answer++;
      break;
    }

    k -= count[i];
    answer++;
    i++;
  }

  return answer;
}

function solution(weights) {
  let answer = 0;
  weights.sort((a, b) => a - b);
  const freq = new Map();

  for (const w of weights) {
    if (freq.has(w)) answer += freq.get(w);

    if ((2 * w) % 3 === 0) {
      const x = (2 * w) / 3;
      if (freq.has(x)) answer += freq.get(x);
    }

    if (w % 2 === 0) {
      const x = w / 2;
      if (freq.has(x)) answer += freq.get(x);
    }

    if ((3 * w) % 4 === 0) {
      const x = (3 * w) / 4;
      if (freq.has(x)) answer += freq.get(x);
    }

    freq.set(w, (freq.get(w) || 0) + 1);
  }

  return answer;
}

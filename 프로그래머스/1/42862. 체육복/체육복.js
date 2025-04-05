function solution(n, lost, reserve) {
  const losted = lost.filter(l => !reserve.includes(l)).sort((a, b) => a - b);
  const reserved = reserve.filter(v => !lost.includes(v)).sort((a, b) => a - b);
  let result = n - losted.length;


  for (let i = 0; i < losted.length; i++) {
    for (let j = 0; j < reserved.length; j++) {
      const gap = Math.abs(losted[i] - reserved[j]);
      if (gap === 1 || gap === 0) {
        result++;
        reserved[j] = 100;
        break;
      }
    }
  }

  return result;
}
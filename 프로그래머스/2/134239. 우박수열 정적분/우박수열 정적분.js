function solution(k, ranges) {
  const yCoords = [k];
  while (k > 1) {
    if (k % 2 === 0) k /= 2;
    else k = k * 3 + 1;
    yCoords.push(k);
  }

  const areas = [];
  for (let i = 0; i < yCoords.length - 1; i++) {
    const area = (yCoords[i] + yCoords[i + 1]) / 2;
    areas.push(area);
  }

  const totalSegments = areas.length;
  const result = [];

  for (const [a, b] of ranges) {
    const start = a;
    const end = totalSegments + b;

    if (start > end) {
      result.push(-1.0);
    } else {
      const sum = areas.slice(start, end).reduce((acc, cur) => acc + cur, 0);
      result.push(sum);
    }
  }

  return result;
}

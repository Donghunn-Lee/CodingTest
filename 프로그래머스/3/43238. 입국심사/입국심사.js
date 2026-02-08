function solution(n, times) {
  let left = 1n;
  let right = BigInt(Math.max(...times)) * BigInt(n);
  let answer = right;

  while (left <= right) {
    const mid = (left + right) / 2n;

    let total = 0n;
    for (const t of times) {
      total += mid / BigInt(t);
    }

    if (total >= BigInt(n)) {
      answer = mid;
      right = mid - 1n;
    } else {
      left = mid + 1n;
    }
  }

  return Number(answer);
}
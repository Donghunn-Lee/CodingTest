function solution(arrayA, arrayB) {
  const gcd = (a, b) => (b === 0 ? a : gcd(b, a % b));
  const gcdOfArray = (arr) => arr.reduce((acc, cur) => gcd(acc, cur));

  const gcdA = gcdOfArray(arrayA);
  const gcdB = gcdOfArray(arrayB);

  const canUse = (g, arr) => {
    for (const n of arr) {
      if (n % g === 0) return false;
    }
    return true;
  };

  let answer = 0;

  if (canUse(gcdA, arrayB)) {
    answer = Math.max(answer, gcdA);
  }

  if (canUse(gcdB, arrayA)) {
    answer = Math.max(answer, gcdB);
  }

  return answer;
}

function isPrime(num) {
  if (num < 2) return false;
  if (num === 2) return true;

  for (let i = 2; i <= Math.floor(Math.sqrt(num)); i++) {
    if (num % i === 0) {
      return false;
    }
  }
  return true;
}

function solution(n, k) {
  let answer = 0;
  let str = n.toString(k);
  let strArray = str.split('0');

  for (let i = 0; i < strArray.length; i++) {
    const cur = +strArray[i];
    if (cur && isPrime(cur)) answer++;
  }

  return answer;
}

solution(110011, 10);

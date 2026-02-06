function solution(number, k) {
  const stack = [];

  for (const digit of number) {
    while (
      k > 0 &&
      stack.length &&
      stack.at(-1) < digit
    ) {
      stack.pop();
      k--;
    }
    stack.push(digit);
  }

  return stack.slice(0, stack.length - k).join('');
}
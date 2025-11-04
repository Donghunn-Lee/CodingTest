function solution(order) {
  let answer = 0;
  const n = order.length;
  const stack = [];
  let incoming = 1;
  let orderIdx = 0;

  while (incoming <= n) {
    stack.push(incoming);

    while (stack.length && stack.at(-1) === order[orderIdx]) {
      stack.pop();
      answer++;
      orderIdx++;
    }

    incoming++;
  }

  while (stack.length && stack[stack.length - 1] === order[orderIdx]) {
    stack.pop();
    answer++;
    orderIdx++;
  }

  return answer;
}

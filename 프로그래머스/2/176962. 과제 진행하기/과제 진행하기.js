function timeToMinute(time) {
  const [h, m] = time.split(':').map(Number);
  return h * 60 + m;
}

function solution(plans) {
  const answer = [];
  const stack = [];

  plans = plans.map(([name, time, duration]) => [name, timeToMinute(time), +duration]);

  plans.sort((a, b) => a[1] - b[1]);

  for (let i = 0; i < plans.length - 1; i++) {
    const [name, start, duration] = plans[i];
    const nextStart = plans[i + 1][1];
    let gap = nextStart - start;

    if (gap >= duration) {
      answer.push(name);
      gap -= duration;

      while (gap > 0 && stack.length > 0) {
        const top = stack[stack.length - 1];
        if (top[1] <= gap) {
          gap -= top[1];
          answer.push(stack.pop()[0]);
        } else {
          top[1] -= gap;
          break;
        }
      }
    } else {
      stack.push([name, duration - gap]);
    }
  }

  answer.push(plans.at(-1)[0]);

  while (stack.length > 0) {
    answer.push(stack.pop()[0]);
  }

  return answer;
}

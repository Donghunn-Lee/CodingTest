function timeToMinute(time) {
  const [h, m] = time.split(':').map(Number);
  return h * 60 + m;
}

function solution(plans) {
  const answer = [];
  const stack = [];

  // 시간 정수화
  plans = plans.map(([name, time, duration]) => [name, timeToMinute(time), +duration]);

  // 시작 시간 기준 정렬
  plans.sort((a, b) => a[1] - b[1]);

  for (let i = 0; i < plans.length - 1; i++) {
    const [name, start, duration] = plans[i];
    const nextStart = plans[i + 1][1];
    let gap = nextStart - start;

    if (gap >= duration) {
      // 현재 과제를 다 끝냄
      answer.push(name);
      gap -= duration;

      // 그 남은 시간 동안 스택 처리
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
      // 다 못 끝내고 중단
      stack.push([name, duration - gap]);
    }
  }

  // 마지막 과제는 무조건 완료됨
  answer.push(plans.at(-1)[0]);

  // 남은 스택 처리
  while (stack.length > 0) {
    answer.push(stack.pop()[0]);
  }

  return answer;
}

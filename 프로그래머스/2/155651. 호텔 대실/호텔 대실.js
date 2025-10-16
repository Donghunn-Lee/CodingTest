function solution(book_time) {
  let answer = 0;

  const events = [];
  for (const [start, end] of book_time) {
    const [sh, sm] = start.split(':').map(Number);
    const [eh, em] = end.split(':').map(Number);
    const s = sh * 60 + sm;
    const e = eh * 60 + em + 10;

    events.push([s, +1]);
    events.push([e, -1]);
  }

  events.sort((a, b) => a[0] - b[0] || a[1] - b[1]);

  let cur = 0;
  for (const [, delta] of events) {
    cur += delta;
    if (cur > answer) answer = cur;
  }
  return answer;
}

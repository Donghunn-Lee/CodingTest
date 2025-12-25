function solution(record) {
  let answer = [];
  const users = {};

  for (const log of record) {
    const [action, id, nickname] = log.split(' ');

    if (action === 'Leave') continue;

    users[id] = { nickname: nickname };
  }

  for (const log of record) {
    let curLog = '';
    const [action, id, _] = log.split(' ');

    if (action === 'Change') continue;

    if (action === 'Enter') {
      curLog = `${users[id].nickname}님이 들어왔습니다.`;
    } else if (action === 'Leave') {
      curLog = `${users[id].nickname}님이 나갔습니다.`;
    }

    answer.push(curLog);
  }

  return answer;
}

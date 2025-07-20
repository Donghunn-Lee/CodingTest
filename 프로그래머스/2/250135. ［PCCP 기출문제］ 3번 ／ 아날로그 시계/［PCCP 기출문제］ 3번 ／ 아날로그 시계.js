function timeToSecond(hours, minutes, seconds) {
  return hours * 60 * 60 + minutes * 60 + seconds;
}

function timeToAngle(s) {
  const hour = parseInt(s / 3600);
  const minute = parseInt((s % 3600) / 60);
  const second = parseInt((s % 3600) % 60);

  // 초침 : 초당 6도
  // 분침 : 초당 0.1도, 분당 6도
  // 시침 : 초당 1/120도, 분당 0.5도, 시간 당 30도

  const hourAngle = (hour % 12) * 30 + minute * 0.5 + second * (1 / 120);
  const minuteAngle = minute * 6 + second * 0.1;
  const secondAngle = second * 6;

  return [hourAngle, minuteAngle, secondAngle];
}

const didHourCross = (curAngle, nxtAngle) => {
  const curHour = curAngle[0];
  const curSecond = curAngle[2];

  const laterHour = nxtAngle[0];
  const laterSecond = nxtAngle[2];

  if (curHour > curSecond && laterHour <= laterSecond) return true;

  if (curSecond === 354 && curHour > 354) return true;

  return false;
};

const didMinuteCross = (curAngle, nxtAngle) => {
  const curMinute = curAngle[1];
  const curSecond = curAngle[2];

  const laterMinute = nxtAngle[1];
  const laterSecond = nxtAngle[2];

  if (curMinute > curSecond && laterMinute <= laterSecond) return true;

  if (curSecond === 354 && curMinute > 354) return true;

  return false;
};

function solution(h1, m1, s1, h2, m2, s2) {
  let answer = 0;

  const startTime = timeToSecond(h1, m1, s1);
  const endTime = timeToSecond(h2, m2, s2);

  if (startTime === 0 || startTime === 43200) answer++;

  for (let t = startTime; t < endTime; t++) {
    const curAngle = timeToAngle(t);
    const nxtAngle = timeToAngle(t + 1);

    const [isMinuteCrossed, isHourCrossed] = [
      didMinuteCross(curAngle, nxtAngle),
      didHourCross(curAngle, nxtAngle),
    ];

    if (isMinuteCrossed && isHourCrossed) {
      if (nxtAngle[0] === nxtAngle[1]) answer += 1;
      else answer += 2;
    } else if (isMinuteCrossed || isHourCrossed) {
      answer += 1;
    }
  }

  return answer;
}

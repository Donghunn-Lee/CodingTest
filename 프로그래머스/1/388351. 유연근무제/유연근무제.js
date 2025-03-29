function solution(schedules, timelogs, startday) {
  let answer = 0;

  for (let i = 0; i < schedules.length; i++) {
    let hours = Math.floor(schedules[i] / 100);
    let minute = schedules[i] % 100;
    let targetTime =
      (hours + Math.floor((minute + 10) / 60)) * 100 + ((minute + 10) % 60);
    let count = 0;

    for (let j = 0; j < 7; j++) {
      let currentDay = (j + startday - 1) % 7;

      if (currentDay === 5 || currentDay === 6) continue;

      if (timelogs[i][j] <= targetTime) {
        count++;
      }
    }

    if (count === 5) answer++;
  }

  return answer;
}
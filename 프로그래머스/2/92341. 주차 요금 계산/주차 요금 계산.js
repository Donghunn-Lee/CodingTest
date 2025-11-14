function toMinutes(time) {
  const [h, m] = time.split(':').map(Number);
  return h * 60 + m;
}

function solution(fees, records) {
  const [baseTime, baseFee, unitTime, unitFee] = fees;

  const inTime = {};
  const totalTime = {};

  for (const rec of records) {
    const [timeStr, car, state] = rec.split(' ');
    const t = toMinutes(timeStr);

    if (totalTime[car] === undefined) totalTime[car] = 0;

    if (state === 'IN') {
      inTime[car] = t;
    } else {
      totalTime[car] += t - inTime[car];
      delete inTime[car];
    }
  }

  const endOfDay = toMinutes('23:59');
  for (const car in inTime) {
    totalTime[car] += endOfDay - inTime[car];
  }

  const cars = Object.keys(totalTime).sort((a, b) => Number(a) - Number(b));

  return cars.map((car) => {
    const t = totalTime[car];
    if (t <= baseTime) return baseFee;

    const extra = t - baseTime;
    const units = Math.ceil(extra / unitTime);
    return baseFee + units * unitFee;
  });
}

function solution(cap, n, deliveries, pickups) {
  let answer = 0;
  let dRemain = 0;
  let pRemain = 0;

  for (let i = n - 1; i >= 0; i--) {
    dRemain += deliveries[i];
    pRemain += pickups[i];

    if (dRemain === 0 && pRemain === 0) continue;

    const trips = Math.ceil(Math.max(dRemain, pRemain) / cap);

    answer += (i + 1) * 2 * trips;

    dRemain -= cap * trips;
    pRemain -= cap * trips;
  }

  return answer;
}
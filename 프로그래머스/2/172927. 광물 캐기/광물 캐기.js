function solution(picks, minerals) {
  let answer = 0;
  const totalPicking = Math.min(
    picks.reduce((acc, val) => acc + val, 0),
    Math.ceil(minerals.length / 5)
  );
  minerals.splice(totalPicking * 5);

  const picksArray = [];
  picks.forEach((val, idx) => {
    for (let i = 0; i < val; i++) {
      picksArray.push(idx);
    }
  });
  picksArray.sort();

  const groupedMinerals = [];
  for (let i = 0; i < totalPicking; i++) {
    const group = { diamond: 0, iron: 0, stone: 0 };
    const mineral = minerals.slice(i * 5, (i + 1) * 5);
    for (let m of mineral) {
      group[m]++;
    }

    groupedMinerals[i] = group;
  }

  const sortedKeys = Object.entries(groupedMinerals)
    .sort(([, v1], [, v2]) => {
      if (v2.diamond !== v1.diamond) return v2.diamond - v1.diamond;
      if (v2.iron !== v1.iron) return v2.iron - v1.iron;
      return v2.stone - v1.stone;
    })
    .map(([key]) => Number(key));

  for (let i = 0; i < totalPicking; i++) {
    let fatigue = 0;
    const { diamond, iron, stone } = groupedMinerals[sortedKeys[i]];
    const pick = picksArray[i];

    if (pick == 0) {
      fatigue += diamond + iron + stone;
    } else if (pick == 1) {
      fatigue += diamond * 5 + iron + stone;
    } else {
      fatigue += diamond * 25 + iron * 5 + stone;
    }

    answer += fatigue;
  }

  return answer;
}
function solution(info, query) {
  let answer = [];
  const hashMap = new Map();

  const makeCombination = (infoArr, score, start) => {
    const key = infoArr.join('');

    if (hashMap.has(key)) hashMap.get(key).push(score);
    else hashMap.set(key, [score]);

    for (let i = start; i < 4; i++) {
      let temp = [...infoArr];
      temp[i] = '-';
      makeCombination(temp, score, i + 1);
    }
  };

  const binarySearch = (arr, target) => {
    let left = 0;
    let right = arr.length;

    while (left < right) {
      const mid = Math.floor((left + right) / 2);

      if (arr[mid] >= target) right = mid;
      else left = mid + 1;
    }

    return left;
  };

  for (const applicant of info) {
    const infoArr = applicant.split(' ');
    const score = +infoArr.pop();
    makeCombination(infoArr, score, 0);
  }

  for (const [key, value] of hashMap) {
    value.sort((a, b) => a - b);
  }

  for (const cmd of query) {
    const cmdArr = cmd.split(' and ');
    const [soulfood, score] = cmdArr.pop().split(' ');
    cmdArr.push(soulfood);
    const targetScore = +score;
    const cmdStr = cmdArr.join('');

    if (hashMap.has(cmdStr)) {
      const arr = hashMap.get(cmdStr);
      const index = binarySearch(arr, targetScore);
      answer.push(arr.length - index);
    } else {
      answer.push(0);
    }
  }

  return answer;
}
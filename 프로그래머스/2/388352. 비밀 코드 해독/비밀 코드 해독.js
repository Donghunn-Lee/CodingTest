const getCombination = (arr, n) => {
  const combination = [];

  const dfs = (rest, s, count) => {
    if (count == 0) {
      combination.push(rest);

      return;
    }

    for (let i = s; i < arr.length; i++) {
      dfs([...rest, arr[i]], i + 1, count - 1);
    }
  };

  dfs([], 0, n);

  return combination;
};

const solution = (n, q, ans) => {
  let answer = 0;
  const numbers = Array.from({ length: n }, (v, i) => i + 1);
  const combination = getCombination(numbers, 5);

  for (let i = 0; i < combination.length; i++) {
    let match = 0;

    for (let j = 0; j < q.length; j++) {
        const count = combination[i].filter((num) => q[j].includes(num)).length;

        if (count == ans[j]) {
            match++;
        }
    }

    if (match == q.length) {
        answer++;
    }
  }

  return answer;
};

function solution(users, emoticons) {
  let maxSubs = 0;
  let maxTake = 0;

  const discounts = [10, 20, 30, 40];

  function calc(discountCombo) {
    let subs = 0;
    let take = 0;

    for (const [ratio, threshold] of users) {
      let total = 0;

      for (let i = 0; i < emoticons.length; i++) {
        const emo = emoticons[i];
        const d = discountCombo[i];
        if (ratio <= d) {
          total += (emo * (100 - d)) / 100;
        }
      }

      if (total >= threshold) subs++;
      else take += total;
    }

    if (subs > maxSubs || (subs === maxSubs && take > maxTake)) {
      maxSubs = subs;
      maxTake = take;
    }
  }

  function dfs(idx, combo) {
    if (idx === emoticons.length) {
      calc(combo);
      return;
    }
    for (const d of discounts) {
      combo[idx] = d;
      dfs(idx + 1, combo);
    }
  }

  dfs(0, []);

  return [maxSubs, maxTake];
}
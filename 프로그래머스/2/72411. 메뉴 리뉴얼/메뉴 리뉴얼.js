function solution(orders, course) {
  let answer = [];
  const sortedOrders = orders.map(order => order.split('').sort().join(''));

  for (const len of course) {
    const map = new Map();
    let maxCount = 0;

    function dfs(order, cur, idx) {
      if (cur.length === len) {
        const count = (map.get(cur) || 0) + 1;
        map.set(cur, count);
        maxCount = Math.max(maxCount, count);
        return;
      }

      if (idx === order.length) return;

      dfs(order, cur + order[idx], idx + 1);
      dfs(order, cur, idx + 1);
    }

    for (const order of sortedOrders) {
      if (order.length >= len) dfs(order, '', 0);
    }

    for (const [key, value] of map) {
      if (value >= 2 && value === maxCount) {
        answer.push(key);
      }
    }
  }

  return answer.sort();
}
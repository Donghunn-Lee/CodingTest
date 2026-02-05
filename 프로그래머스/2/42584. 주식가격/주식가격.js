function solution(prices) {
  const n = prices.length;
  const answer = Array(n).fill(0);
  const st = [];
    
  for (let i = 0; i < n; i++) {
    while (st.length && prices[i] < prices[st[st.length - 1]]) {
      const j = st.pop();
      answer[j] = i - j;
    }
    st.push(i);
  }

  while (st.length) {
    const j = st.pop();
    answer[j] = (n - 1) - j;
  }

  return answer;
}
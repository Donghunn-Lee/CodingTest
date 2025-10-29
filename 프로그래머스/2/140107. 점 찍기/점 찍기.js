function solution(k, d) {
  const dd = d * d;
  let ans = 0;

  for (let x = 0; x <= d; x += k) {
    const remain = dd - x * x;
    const yMax = Math.floor(Math.sqrt(remain) / k);
      
    ans += (yMax + 1);
  }
    
  return ans;
}
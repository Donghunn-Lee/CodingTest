function solution(s) {
  const nums = s.match(/\d+/g);
  
  const counts = {};
  for (const num of nums) {
    counts[num] = (counts[num] || 0) + 1;
  }

  return Object.keys(counts)
    .sort((a, b) => counts[b] - counts[a])
    .map(Number);
}
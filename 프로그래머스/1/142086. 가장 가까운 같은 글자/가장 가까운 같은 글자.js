function solution(s) {
  var answer = [];
  
  const nearChar = {};
  
  for (let i = 0; i < s.length; i++) {
      if (nearChar[s[i]] === undefined) {
          answer.push(-1);
          nearChar[s[i]] = i;
      } else {
          answer.push(i - nearChar[s[i]]);
          nearChar[s[i]] = i;
      }
  }
  
  
  return answer;
}

console.log(solution("banana"));
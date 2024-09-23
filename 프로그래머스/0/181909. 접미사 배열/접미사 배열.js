function solution(my_string) {
  var answer = [];
  let tmp = '';
  
  for (let i = 1; i <= my_string.length; i++) {
      tmp = my_string.at(-i) + tmp;
      answer.push(tmp);
  }
  
  answer.sort();
  
  return answer;
}
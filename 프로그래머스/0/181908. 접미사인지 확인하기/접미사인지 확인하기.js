function solution(my_string, is_suffix) {
  var answer = [];
  let tmp = '';
  
  for (let i = 1; i <= my_string.length; i++) {
      tmp = my_string.at(-i) + tmp;
      answer.push(tmp);
  }
  
  if (answer.includes(is_suffix)) {
      return 1;
  } else {
      return 0
  }  
}
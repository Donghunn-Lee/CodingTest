function solution(my_string, s, e) {
  let arr = [...my_string];
  arr.splice(s, e - s + 1, ...arr.slice(s, e + 1).reverse());
  
  return arr.join("");
}
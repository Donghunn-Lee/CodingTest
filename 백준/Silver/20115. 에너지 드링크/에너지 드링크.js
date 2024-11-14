const [, input] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const drinks = input
  .split(' ')
  .map(val => +val)
  .sort((a, b) => a - b);

const getMaxEnergy = () => {
  // drinks 배열에 하나의 음료수만 남을 때까지
  while (drinks.length > 1) {
  	// drinks 배열은 정렬되어 있기 때문에 제일 마지막 값이 제일 큰 값이다
    const bigger = drinks.pop();
    const smaller = drinks.pop();
    // 더 작은 음료수의 반을 흘린고, 더 큰 음료수와 합친 후 drinks 배열에 넣어준다
    const combined = bigger + smaller * 0.5;

    drinks.push(combined);
  }

  return drinks[0];
};

console.log(getMaxEnergy());
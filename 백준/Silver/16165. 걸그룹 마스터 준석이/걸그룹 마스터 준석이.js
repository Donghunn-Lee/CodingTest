const [in1, ...in2] = require('fs')
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split('\n');

const [N, M] = in1.split(' ').map(Number);

// 전역에 객체를 생성하고, 키값은 그룹명, 밸류값은 멤버명이 담긴 배열
const data = {};

// data 완성
for (let i = 0; i < N; i++) {
  const teamName = in2.shift();
  const memberNum = +in2.shift();
  data[teamName] = in2.splice(0, memberNum);
}

const answer = [];

// 제시되는 조건에 따라 답을 리턴하는 함수
const tester = (keyword, type) => {
  if (type) {
    for (let team in data) {
      if (data[team].includes(keyword)) return team;
    }
  }
  for (let team in data) {
  	// 팀 멤버 전체를 리턴하는 경우, 줄바꿈해서 리턴
    if (keyword === team) return data[team].sort().join('\n');
  }
};

for (let i = 0; i < M; i++) {
  const keyword = in2.shift();
  const type = +in2.shift();
  answer.push(tester(keyword, type));
}

console.log(answer.join('\n'));
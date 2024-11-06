const [N, ...straws] = require('fs').readFileSync('/dev/stdin')
                       .toString().trim().split("\n").map(v => +v);
const sortedStraws = straws.sort((a,b) => b-a); // 내림차순 정렬.

const findAns = () => {
  while(true){
    const maxLine = sortedStraws[0];
    const sumLines = sortedStraws[1] + sortedStraws[2];
    
    // 삼각형을 만들 수 있다면 세 변의 길이 합 리턴. 아니라면 최댓값을 빼고 반복문 계속.
    if(maxLine < sumLines) return maxLine + sumLines;
    else sortedStraws.shift(); 

    // 만약 삼각형을 만들 수 없을 정도로 변의 개수가 적어진다면 -1 
    if(sortedStraws.length < 3) return -1; 
  }
}

console.log(findAns());
function solution(answers) {
  let result = [];
  const scores = Array(3).fill(0);
  const std1 = [1,2,3,4,5];
  const std2 = [2,1,2,3,2,4,2,5];
  const std3 = [3,3,1,1,2,2,4,4,5,5];
  const students = [std1, std2, std3]
  
  const gradeQuestion = (std, i) => {
      if (std[i % std.length] === answers[i]) {
          return true;
      }
      
      return false;
  }
  
  answers.forEach((answer, i) => {
      for (let j = 0; j < 3; j++) {
          if (gradeQuestion(students[j], i)) {
              scores[j]++;
          }    
      }
  })
  
  const maxScore = Math.max(...scores);
  
  scores.forEach((score, i) => {
      if (score == maxScore) result.push(i + 1);
  })
  
  return result;
}
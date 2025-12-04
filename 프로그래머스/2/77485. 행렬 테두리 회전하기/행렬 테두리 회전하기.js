function solution(rows, columns, queries) {
  const answer = [];

  // 1. 초기 행렬 생성
  const matrix = Array.from({ length: rows }, (_, r) =>
    Array.from({ length: columns }, (_, c) => r * columns + (c + 1))
  );

  // 2. 쿼리 하나씩 처리
  for (const query of queries) {
    // 0-based index로 수정
    const [x1, y1, x2, y2] = query.map((val) => val - 1);

    // 좌측 상단 값 저장
    const temp = matrix[x1][y1];
    let minVal = temp; // 이번 로테이션 최솟값

    // 1) 좌측 열 상단으로 당기기
    for (let i = x1; i < x2; i++) {
      matrix[i][y1] = matrix[i + 1][y1];
      minVal = Math.min(minVal, matrix[i][y1]);
    }

    // 2) 하단 행 좌측으로 당기기
    for (let i = y1; i < y2; i++) {
      matrix[x2][i] = matrix[x2][i + 1];
      minVal = Math.min(minVal, matrix[x2][i]);
    }

    // 3) 우측 행 하단으로 당기기
    for (let i = x2; i > x1; i--) {
      matrix[i][y2] = matrix[i - 1][y2];
      minVal = Math.min(minVal, matrix[i][y2]);
    }

    // 4) 상단 행 우측으로 당기기
    for (let i = y2; i > y1; i--) {
      matrix[x1][i] = matrix[x1][i - 1];
      minVal = Math.min(minVal, matrix[x1][i]);
    }

    // 5) 좌측 상단 (x1, y1 + 1)칸 채우기
    matrix[x1][y1 + 1] = temp;

    // 최솟값 배열에 추가
    answer.push(minVal);
  }

  return answer;
}

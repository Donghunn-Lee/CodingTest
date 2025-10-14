function solution(board) {
  // 개수 세기
  let o = 0, x = 0;
  for (let i = 0; i < 3; i++) {
    for (let j = 0; j < 3; j++) {
      if (board[i][j] === 'O') o++;
      else if (board[i][j] === 'X') x++;
    }
  }

  // 기본 개수 규칙
  if (x > o) return 0;
  if (o - x > 1) return 0;

  // 승리 판단 함수
  const win = (ch) => {
    // 가로
    for (let i = 0; i < 3; i++) {
      if (board[i][0] === ch && board[i][1] === ch && board[i][2] === ch) return true;
    }
    // 세로
    for (let i = 0; i < 3; i++) {
      if (board[0][i] === ch && board[1][i] === ch && board[2][i] === ch) return true;
    }
    // 대각
    if (board[0][0] === ch && board[1][1] === ch && board[2][2] === ch) return true;
    if (board[0][2] === ch && board[1][1] === ch && board[2][0] === ch) return true;
    return false;
  };

  const oWin = win('O');
  const xWin = win('X');

  // 둘 다 이김 → 불가
  if (oWin && xWin) return 0;

  // 누가 이겼는지에 따른 턴수 일관성 검사
  if (oWin && o !== x + 1) return 0;
  if (xWin && o !== x) return 0;

  return 1;
}
function solution(board, moves) {
  let result = 0;
  const basket = [];

  const clawing = (n) => {
    for (let i = 0; i < board.length; i++) {
      if (board[i][n]) {
        putDown(board[i][n]);
        board[i][n] = 0;
        
        return;
      }
    }
  };

  const putDown = (t) => {
    if (t === basket.at(-1)) {
      basket.pop();
      result += 2;
    } else {
      basket.push(t);
    }
  };

  moves.forEach((v) => {
    clawing(v - 1);
  });

  return result;
}
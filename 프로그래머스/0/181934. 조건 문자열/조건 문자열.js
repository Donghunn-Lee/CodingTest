function solution(ineq, eq, n, m) {
    if (eq === '=') {
        if (ineq === '>') {
            return n >= m ? 1 : 0;
        } else {
            return n <= m ? 1 : 0;
        }
    } else {
        if (ineq === '>') {
            return n > m ? 1 : 0;
        } else {
            return n < m ? 1 : 0;
        }
    }
}
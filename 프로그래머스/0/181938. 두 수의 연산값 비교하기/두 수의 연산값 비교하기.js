function solution(a, b) {
    return +(`${a}` + `${b}`) < 2 * a * b ? 2 * a * b : +(`${a}` + `${b}`);
}
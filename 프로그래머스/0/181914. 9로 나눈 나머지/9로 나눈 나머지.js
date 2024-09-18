function solution(number) {
    return [...number].reduce((acc, val) => acc + Number(val), 0) % 9;
}
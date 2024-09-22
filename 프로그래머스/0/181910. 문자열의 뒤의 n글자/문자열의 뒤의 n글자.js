function solution(my_string, n) {
    return [...my_string].splice(my_string.length - n, n).join("");
}
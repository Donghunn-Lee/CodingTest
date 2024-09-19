function solution(my_string, queries) {
    for (let q of queries) {
        let [s, e] = q;
        
        my_string = my_string.slice(0, s) + [...my_string.slice(s, e + 1)].reverse().join("") + my_string.slice(e + 1);
    }
    
    return my_string;
}
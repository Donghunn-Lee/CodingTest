function solution(str, queries) {
    str = [...str];
    
    for (let q of queries) {
        let [s, e] = q;
        
        str.splice(s, e - s + 1, ...str.slice(s, e + 1).reverse())
    }
    
    return str.join("");
}
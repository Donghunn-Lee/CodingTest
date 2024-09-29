function solution(my_string, is_prefix) {
    const subfix = [];
    let tmp = '';
    
    for (let i = 0; i < my_string.length; i++) {
        tmp += my_string[i];
        subfix.push(tmp);
    }
    
    if (subfix.includes(is_prefix)) {
        return 1;
    } else {
        return 0;
    }
}
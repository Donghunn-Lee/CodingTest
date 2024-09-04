function solution(n, control) {
    for (let cmd of control) {
        if (cmd == 'w') n++;
        else if (cmd == 's') n--;
        else if (cmd == 'd') n += 10;
        else if (cmd == 'a') n -= 10;
    }
    return n;    
}